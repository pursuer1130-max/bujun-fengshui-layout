# 卜君风水布局

以书籍正文、已有案例和可观察空间关系为依据的中文Agent Skill。支持阳宅、阴宅知识学习、整体格局论证、实际图片标注和专业报告。

**v8 · 2026-10-30。现行已有案例学习目标不少于100,000例，尚未完成。** 当前发布的是已读书籍知识与已验证功能，书目、篇卷、论坛主题和合成训练行不计作已读案例。

## 阳宅与阴宅

- [阳宅](fengshui-photo/references/yangzhai.md)：住宅、别墅、高层单元、单间、办公室与店铺；从外局与门路连到主位、寝居、炊事、动静和方案代价。
- [阴宅](fengshui-photo/references/yinzhai.md)：墓地、墓园、历史墓园和骨灰安置空间；论远势近形、高山平洋、龙穴砂水向、明堂水口及观察基点，使用专用报告。
- 用户看图时实际标注并展示成品；纯知识与读书请求无需图片。图像能力和编辑工具由宿主提供。

## 实际读书范围

全文读本地《宅经》四库本上下卷网页转录，选读《阳宅十书》外形/福元/放水/内形相关篇、《葬书》《撼龙经》《疑龙经·上篇》段落；另读《相宅书叙》两叶和《雪心赋》个人录文选段。均未冒作影印底本校勘或全部传本通读。《阳宅三要》原刻仅核版本，正文未读。

读书记录：[阳宅](fengshui-photo/references/book-reading-yang.json) · [阴宅](fengshui-photo/references/book-reading-yin.json) · [书籍来源核查](fengshui-photo/references/book-source-checks.md)。

## 安装与使用

把本仓库的 `fengshui-photo` 整个文件夹复制到 `~/.agents/skills/`，使其直接包含SKILL.md。显示名“卜君风水布局”，技术调用名保持兼容：

```text
使用 $fengshui-photo，直接依据已读书籍解释阳宅门、主、灶的整体取舍，并标明所用版本。
使用 $fengshui-photo，分析这张墓地照片的形势，给出专业且通俗的报告，并实际展示标注图。
```

其他AI可导入技能目录，或使用[通用提示词](fengshui-photo/portable/通用风水看图提示词.md)。没有视觉或文件工具时按实际能力使用，提示词不会自动增加工具。

## 知识与进度

保留16类场景知识、12组外局/商业正文材料、6项方法比较、29项基础书目和9页古籍转录。旧账本60条材料中37条是合格具体短笔记；教学、实践自述、空间参照与研究样本分列。本轮读书新增案例数0，不代表训练了底层模型。

[技能入口](fengshui-photo/SKILL.md) · [整体研判](fengshui-photo/references/layout-assessment.md) · [十万目标实际进度](fengshui-photo/references/cases/corpus-progress.md) · [来源审计](fengshui-photo/references/cases/hundredk-sources.md)。

古《宅经》的阴阳分类按原书语境保留，不全数等同现代住宅/墓地。没有自动飞星、命卦、分金引擎；不从照片补造方位、年代或宅盘，不把传统断语当成已验证的人事因果。

## 许可与验证

[许可](LICENSE.md) · [第三方说明](THIRD_PARTY_NOTICES.md) · [验证范围](VALIDATION.md)。古籍转录保留贡献者、固定修订与适用许可。当前发行不含研究联系表图像或客户照片，仅保留原数据链接与历史读图记录。`SHA256SUMS`可核技能文件完整性。
