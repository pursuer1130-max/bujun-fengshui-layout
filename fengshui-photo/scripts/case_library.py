#!/usr/bin/env python3
"""Offline audit and retrieval of provenance-linked feng shui case notes.

This verifies recorded evidence declarations, not whether a reviewer truly read a
page, saw an image, or verified an outcome. It never fetches sources or trains a
model. Duplicate candidates are evidence for review, not semantic merge orders.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

DEFAULT_INPUT = Path(__file__).resolve().parents[1] / "references" / "cases" / "cases.jsonl"
KIND_ALIASES = {
    "real_claimed": "practice", "reported_practice": "practice",
    "teaching_example": "teaching", "teaching": "teaching",
    "spatial_reference": "spatial_reference", "ordinary_layout": "spatial_reference",
    "general_advice": "general_advice", "unknown": "unknown",
}
STUDY_STATES = {"discovered", "retrieved", "screened", "text_reviewed", "visual_reviewed", "held_out", "excluded"}
IMAGE_STATES = {"not_present", "link_only", "fetch_failed", "rendered_unreviewed", "visually_reviewed", "unknown"}
BODY_STATES = {"read", "partial", "blocked", "error", "not_read", "unknown"}
DUPLICATE_STATES = {"not_checked", "unique", "merged", "uncertain"}
TRACKING_KEYS = {"fbclid", "gclid", "dclid", "msclkid", "spm", "mc_cid", "mc_eid"}
REVIEWED = {"text_reviewed", "visual_reviewed"}


class CaseDataError(ValueError):
    def __init__(self, errors):
        self.errors = errors
        super().__init__("; ".join(errors))


def normalized_text(value):
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def normalize_url(value):
    """Remove known tracking and fragments; keep content-changing query keys.

    Do not assume www/non-www or http/https hosts are interchangeable.
    """
    p = urlsplit(value.strip())
    host = (p.hostname or "").lower()
    if ":" in host:
        host = "[" + host + "]"
    port = p.port
    if port and not ((p.scheme.lower() == "https" and port == 443) or (p.scheme.lower() == "http" and port == 80)):
        host += ":" + str(port)
    pairs = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True)
             if not k.casefold().startswith("utm_") and k.casefold() not in TRACKING_KEYS]
    return urlunsplit((p.scheme.lower(), host, p.path or "/", urlencode(sorted(pairs)), ""))


def load_records(path):
    path = Path(path)
    try:
        raw = path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        raise CaseDataError([f"{path}: {exc}"]) from exc
    if not raw.strip():
        return [], []
    if raw.lstrip().startswith("["):
        try:
            records = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise CaseDataError([f"{path}: line {exc.lineno}: {exc.msg}"]) from exc
        return records, [f"{path}: array record {i + 1}" for i in range(len(records))]
    records, locations = [], []
    for line_no, line in enumerate(raw.splitlines(), 1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise CaseDataError([f"{path}: line {line_no}: {exc.msg}"]) from exc
        locations.append(f"{path}: line {line_no}")
    return records, locations


def validate_records(records, locations=None):
    errors, seen_ids = [], set()
    if not isinstance(records, list):
        raise CaseDataError(["input must be a JSON array or JSONL records"])
    for i, r in enumerate(records):
        loc = locations[i] if locations else f"record {i + 1}"
        if not isinstance(r, dict):
            errors.append(f"{loc}: expected an object")
            continue
        loc += f" [record_id={r.get('record_id', '<missing>')}]"

        def issue(message):
            errors.append(f"{loc}: {message}")

        for key in ("record_id", "case_group_id", "canonical_url", "source_title"):
            if not isinstance(r.get(key), str) or not r[key].strip():
                issue(f"{key} must be a nonempty string")
        rid = r.get("record_id")
        if isinstance(rid, str):
            if rid in seen_ids:
                issue("duplicate record_id")
            seen_ids.add(rid)
        try:
            url_value = r.get("canonical_url", "")
            p = urlsplit(url_value if isinstance(url_value, str) else "")
            if p.scheme.lower() not in {"http", "https"} or not p.hostname or p.username or p.password:
                issue("canonical_url must be a public HTTP(S) URL without credentials")
            _ = p.port
        except (ValueError, TypeError):
            issue("canonical_url is malformed")
        if not isinstance(r.get("record_kind"), str) or r["record_kind"] not in KIND_ALIASES:
            issue("record_kind is not a supported classification")
        if not isinstance(r.get("study_status"), str) or r["study_status"] not in STUDY_STATES:
            issue("study_status is not supported")
        if not isinstance(r.get("split"), str) or r["split"] not in {"development", "evaluation", "quarantine"}:
            issue("split must be development, evaluation, or quarantine")
        if "source_section" in r and r["source_section"] is not None and not isinstance(r["source_section"], str):
            issue("source_section must be a string or null")
        access = r.get("access")
        if not isinstance(access, dict):
            issue("access must be an object")
            access = {}
        if not isinstance(access.get("body"), str) or access["body"] not in BODY_STATES:
            issue("access.body is not supported")
        if not isinstance(access.get("images"), str) or access["images"] not in IMAGE_STATES:
            issue("access.images is not supported")
        if access.get("body_url") is not None:
            try:
                body_url = access["body_url"]
                q = urlsplit(body_url if isinstance(body_url, str) else "")
                if q.scheme.lower() not in {"http", "https"} or not q.hostname or q.username or q.password:
                    issue("access.body_url must be the actual public HTTP(S) page read")
                _ = q.port
            except (ValueError, TypeError):
                issue("access.body_url is malformed")
        dup = r.get("duplicate_decision")
        if not isinstance(dup, dict) or not isinstance(dup.get("status"), str) or dup["status"] not in DUPLICATE_STATES:
            issue("duplicate_decision.status is not supported")
        if not isinstance(r.get("review_notes"), str):
            issue("review_notes must be a string; leave empty only for unreviewed candidates")
        for key in ("observations", "claims", "actions", "unknowns", "tags"):
            if not isinstance(r.get(key), list):
                issue(f"{key} must be an array")
        for key in ("unknowns", "tags"):
            if isinstance(r.get(key), list) and any(not isinstance(x, str) for x in r[key]):
                issue(f"{key} must contain strings")
        observations = r.get("observations", [])
        obs_ids = set()
        if isinstance(observations, list):
            for n, o in enumerate(observations, 1):
                if not isinstance(o, dict):
                    issue(f"observations[{n}] must be an object")
                    continue
                for key in ("id", "anchor", "summary"):
                    if not isinstance(o.get(key), str) or not o[key].strip():
                        issue(f"observations[{n}].{key} must be a nonempty string")
                if not isinstance(o.get("basis"), str) or o["basis"] not in {"source_text", "viewed_image"}:
                    issue(f"observations[{n}].basis must be source_text or viewed_image")
                if isinstance(o.get("id"), str):
                    if o["id"] in obs_ids:
                        issue(f"observations[{n}].id is duplicated")
                    obs_ids.add(o["id"])
        claims = r.get("claims", [])
        if isinstance(claims, list):
            for n, c in enumerate(claims, 1):
                if not isinstance(c, dict) or not isinstance(c.get("summary"), str) or not c["summary"].strip():
                    issue(f"claims[{n}] must be an object with a nonempty summary")
                    continue
                refs = c.get("observation_ids", [])
                if not isinstance(refs, list) or any(not isinstance(x, str) or x not in obs_ids for x in refs):
                    issue(f"claims[{n}].observation_ids must refer to existing observations")
        if isinstance(r.get("actions"), list):
            for n, a in enumerate(r["actions"], 1):
                if not isinstance(a, dict) or not isinstance(a.get("summary"), str) or not a["summary"].strip():
                    issue(f"actions[{n}] must be an object with a nonempty summary")
        fingerprint = r.get("body_fingerprint")
        if fingerprint is not None and (not isinstance(fingerprint, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", fingerprint)):
            issue("body_fingerprint must be a SHA-256 hex string or null")
        if "near_duplicate_candidates" in r and (not isinstance(r["near_duplicate_candidates"], list) or
                                                   any(not isinstance(x, str) for x in r["near_duplicate_candidates"])):
            issue("near_duplicate_candidates must be an array of record IDs")
        # These are integrity errors, rather than silently downgraded learning.
        if isinstance(r.get("study_status"), str) and r["study_status"] in REVIEWED:
            if access.get("body") != "read":
                issue("reviewed cases require access.body=read")
            if not isinstance(r.get("review_notes"), str) or not r["review_notes"].strip():
                issue("reviewed cases require original review_notes")
            if not isinstance(observations, list) or not observations:
                issue("reviewed cases require at least one anchored observation")
        if r.get("study_status") == "visual_reviewed":
            if access.get("images") != "visually_reviewed":
                issue("visual_reviewed requires access.images=visually_reviewed")
            if not any(isinstance(o, dict) and o.get("basis") == "viewed_image" for o in (observations if isinstance(observations, list) else [])):
                issue("visual_reviewed requires an actual viewed_image observation with an anchor")
    if errors:
        raise CaseDataError(errors)


def _reviewed(r):
    return (r["study_status"] in REVIEWED and r["access"]["body"] == "read" and
            r["split"] == "development" and r["duplicate_decision"]["status"] in {"unique", "merged"})


def duplicate_candidates(records):
    by_group, by_url, by_source_section, by_hash = (defaultdict(list) for _ in range(4))
    for r in records:
        by_group[r["case_group_id"]].append(r)
        url = normalize_url(r["canonical_url"])
        section = normalized_text(r.get("source_section") or "")
        by_url[url].append(r)
        by_source_section[(url, section)].append(r)
        if r.get("body_fingerprint"):
            by_hash[r["body_fingerprint"].lower()].append(r)

    def listing(groups, key_label):
        return [{key_label: str(k), "record_ids": [r["record_id"] for r in rs],
                 "case_group_ids": sorted({r["case_group_id"] for r in rs})}
                for k, rs in groups.items() if len(rs) > 1]

    # Same URL + section with different case IDs is unresolved evidence. Do not
    # merge it semantically; withhold its learning count pending group review.
    collisions = [{"canonical_url": url, "source_section": section or None,
                   "record_ids": [r["record_id"] for r in rs],
                   "case_group_ids": sorted({r["case_group_id"] for r in rs})}
                  for (url, section), rs in by_source_section.items()
                  if len({r["case_group_id"] for r in rs}) > 1]
    return {
        "same_case_group": listing(by_group, "case_group_id"),
        "same_source_page": listing(by_url, "canonical_url"),
        "unresolved_same_source_section": collisions,
        "same_body_fingerprint": listing(by_hash, "sha256"),
        "declared_near_duplicates": [{"record_id": r["record_id"], "candidates": r["near_duplicate_candidates"]}
                                     for r in records if r.get("near_duplicate_candidates")],
        "policy": "Same page or page hash can contain distinct subcases. Only explicit case_group_id merges projects. Same URL+section across different groups is withheld for review; near/text-hash candidates never auto-merge.",
    }


def audit_records(records, target=10001, locations=None):
    if not isinstance(target, int) or target <= 0:
        raise CaseDataError(["target must be a positive integer"])
    validate_records(records, locations)
    duplicates = duplicate_candidates(records)
    collision_groups = {g for c in duplicates["unresolved_same_source_section"] for g in c["case_group_ids"]}
    all_groups = defaultdict(list)
    for r in records:
        all_groups[r["case_group_id"]].append(r)
    split_conflicts = [{"case_group_id": gid, "splits": sorted({r["split"] for r in rs}),
                        "record_ids": [r["record_id"] for r in rs]}
                       for gid, rs in all_groups.items()
                       if len({r["split"] for r in rs}) > 1 or
                       (any(r["study_status"] == "held_out" for r in rs) and any(_reviewed(r) for r in rs))]
    withheld_groups = collision_groups | {c["case_group_id"] for c in split_conflicts}
    groups = defaultdict(list)
    for r in records:
        if _reviewed(r) and r["case_group_id"] not in withheld_groups:
            groups[r["case_group_id"]].append(r)
    classified = defaultdict(set)
    conflicts, visual = [], set()
    for group_id, rs in groups.items():
        kinds = {KIND_ALIASES[r["record_kind"]] for r in rs}
        if len(kinds) != 1:
            conflicts.append({"case_group_id": group_id, "kinds": sorted(kinds), "record_ids": [r["record_id"] for r in rs]})
            continue
        kind = next(iter(kinds))
        classified[kind].add(group_id)
        if kind in {"practice", "teaching"} and any(
            r["study_status"] == "visual_reviewed" and r["access"]["images"] == "visually_reviewed" and
            any(o["basis"] == "viewed_image" for o in r["observations"]) for r in rs
        ):
            visual.add(group_id)
    learned = classified["practice"] | classified["teaching"]
    counts = {
        "discovered_records": len(records),
        "discovered_urls": len({normalize_url(r["canonical_url"]) for r in records}),
        "body_read_pages": len({normalize_url(r["access"].get("body_url") or r["canonical_url"]) for r in records if r["access"]["body"] == "read"}),
        "text_reviewed_unique_practice": len(classified["practice"]),
        "text_reviewed_unique_teaching": len(classified["teaching"]),
        "text_reviewed_unique_spatial_reference": len(classified["spatial_reference"]),
        "qualified_fengshui_cases": len(learned),
        "visual_reviewed_fengshui_cases": len(visual),
        "excluded_records": sum(r["study_status"] == "excluded" for r in records),
        "quarantined_records": sum(r["split"] == "quarantine" for r in records),
        "held_out_records": sum(r["study_status"] == "held_out" or r["split"] == "evaluation" for r in records),
        "repeated_group_records": len(records) - len({r["case_group_id"] for r in records}),
        "unresolved_duplicate_records": sum(r["duplicate_decision"]["status"] in {"not_checked", "uncertain"} for r in records),
        "source_collision_groups_withheld": len(collision_groups),
        "split_conflict_groups_withheld": len(split_conflicts),
    }
    return {"schema_version": 1, "status": "valid", "target_cases": target,
            "target_met": len(learned) >= target, "shortfall": max(0, target - len(learned)),
            "counts": counts, "classification_conflicts_withheld": conflicts,
            "split_conflicts_withheld": split_conflicts,
            "duplicate_candidates": duplicates,
            "limitations": ["Counts audit recorded review declarations; they do not prove reading or image inspection happened.",
                            "Author-reported outcomes are not independently verified and do not establish causal feng shui effects.",
                            "Practice and teaching cases are separate; spatial references, held-out, excluded and quarantine records do not meet the learning target."]}


def search_records(records, query="", tags=None, limit=5):
    validate_records(records)
    terms = [normalized_text(x) for x in query.split() if x.strip()]
    tags = {normalized_text(x) for x in (tags or []) if x.strip()}
    if not terms and not tags:
        raise CaseDataError(["search requires --query or --tags"])
    if not 1 <= limit <= 100:
        raise CaseDataError(["limit must be between 1 and 100"])
    audit = audit_records(records)
    withheld = {g for c in audit["duplicate_candidates"]["unresolved_same_source_section"] for g in c["case_group_ids"]}
    withheld |= {c["case_group_id"] for c in audit["classification_conflicts_withheld"]}
    withheld |= {c["case_group_id"] for c in audit["split_conflicts_withheld"]}
    found = []
    for r in records:
        if not _reviewed(r) or r["case_group_id"] in withheld or KIND_ALIASES[r["record_kind"]] not in {"practice", "teaching", "spatial_reference"}:
            continue
        haystack = normalized_text(" ".join([r["source_title"], r["review_notes"], *r["tags"], *r["unknowns"],
                                               *(o["summary"] for o in r["observations"]),
                                               *(c["summary"] for c in r["claims"]), *(a["summary"] for a in r["actions"])]))
        own_tags = {normalized_text(x) for x in r["tags"]}
        score = sum(1 for term in terms if term in haystack) + 3 * len(tags & own_tags)
        if score and (not tags or tags & own_tags):
            found.append((score, r))
    found.sort(key=lambda x: (-x[0], x[1]["record_id"]))
    hits, seen = [], set()
    for score, r in found:
        if r["case_group_id"] in seen:
            continue
        seen.add(r["case_group_id"])
        hits.append({"record_id": r["record_id"], "case_group_id": r["case_group_id"],
                     "record_kind": r["record_kind"], "source_title": r["source_title"],
                     "source_url": r["canonical_url"], "source_section": r.get("source_section"),
                     "body_read_url": r["access"].get("body_url") or r["canonical_url"],
                     "score": score, "tags": r["tags"], "observations": r["observations"],
                     "author_claims": r["claims"], "actions": r["actions"], "unknowns": r["unknowns"],
                     "review_notes": r["review_notes"], "evidence_status": r["access"],
                     "related_record_ids": [x["record_id"] for x in records if x["case_group_id"] == r["case_group_id"]]})
        if len(hits) >= limit:
            break
    return {"status": "candidates_only", "query": query, "tags": sorted(tags), "hits": hits,
            "warning": "These are source-linked reading notes, not verified predictions or proof of health, wealth or life outcomes. Source-text observations must not be presented as images personally inspected."}


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="UTF-8 JSON array or JSONL")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("audit", "search"):
        p = sub.add_parser(name)
        p.add_argument("--input", type=Path, default=argparse.SUPPRESS)
        if name == "audit":
            p.add_argument("--target", type=int, default=10001)
            p.add_argument("--require-target", action="store_true", help="exit 2 if valid but target is unmet")
        else:
            p.add_argument("--query", default="")
            p.add_argument("--tags", nargs="*", default=[])
            p.add_argument("--limit", type=int, default=5)
    args = parser.parse_args(argv)
    try:
        records, locations = load_records(args.input)
        validate_records(records, locations)
        if args.command == "audit":
            result = audit_records(records, args.target, locations)
        else:
            tags = [tag.strip() for value in args.tags for tag in value.split(",") if tag.strip()]
            result = search_records(records, args.query, tags, args.limit)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 2 if args.command == "audit" and args.require_target and not result["target_met"] else 0
    except CaseDataError as exc:
        print(json.dumps({"status": "invalid", "errors": exc.errors}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
