# 本地案例短笔记索引

原账本日期：2026-10-26；发行范围更新：2026-10-30。保存来源与原创短笔记，历史看图记录逐案保留；当前发行包不含研究联系表图片，只链接原数据。正文、图片是否实际读看分别标明。

**这里统计本包已整理的短笔记，不是外部已有记载的规模或整个skill的完成率。** 查已有案例集、档案与万级研究记录，请用[资料入口](recorded-sources.md)；直接解释场景用[场景知识](patterns.md)。

| 指标 | 实际数 |
|---|---:|
| 可计入目标的具体风水案例 | 37 |
| 其中实践自述/译述及具体布局问答 | 31 |
| 其中明确教学案例 | 6 |
| 上述案例已实际看过原配图 | 2 |
| 普通空间/研究视觉参照（不计目标） | 15 |
| 其中已看图的客家建筑研究图 | 14 |
| 隔离反例（不计目标） | 4 |
| 资料不足暂缓计数 | 3 |
| 来源真实性待核的情境 | 1 |
| 独立结果核验 | 0 |

本轮新增14条记录，其中11条达到具体布局门槛，3条已读客户故事因缺位置关系暂缓计数；26例增至37例。60条总记录不能等同60个合格案例。31个实践类含作者自述、1条阴宅译述及未证实实施的论坛布局问答，不等于31个已经验证的成功改造；6个教学例另列。实际看图的2例是低清外阶教学图，不是住宅勘验图片。

计数来自[统计](stats.json)。正文有图链不等于看过图；网页或匿名客户的真实性及作者所称效验尚无独立验证。当前生成的客厅/卧室标注示例是本项目原创分析，不计第三方已有案例。

## 查阅


- [学习规则与案例适用条件](learning.md)：可变家具、多门用途、素材图、投影尺度、时间线及流派数值差异。
- [逐案原创记录](cases.jsonl)：JSONL，每行一个记录；观察、作者主张、动作、未知项分别保存。
- [来源审计](source-audit.json)：公开数据集、论文样本及论坛候选池的核验边界。

有Python时从技能目录运行：

```text
python scripts/case_library.py search --query "沙发床 通道" --limit 3
python scripts/case_library.py search --tags 入口 餐馆 --limit 3
```

旧审计的target/shortfall是本地短笔记阈值；它不衡量现有资料覆盖，也不要求新做万份分析。脚本只能核查记录结构与声明，不能自动证明实际研读发生。检索结果按案例归组，显示来源与证据类型；不要把检索分数当准确率。无Python时查下表与JSONL即可。


## 记录目录

| ID | 简题 | 类型/状态 | 实际证据 | 来源 |
|---|---|---|---|---|
| WEB-HH-001 | 店铺开在粪池前，生意不减 | 实践/问答自述 | 文字；原图未看 | [原来源](https://honghaometaphysics.weebly.com/blog/8517074) |
| WEB-HH-002 | 独开大门在后巷的商铺 | 实践/问答自述 | 文字；原图未看 | [原来源](https://honghaometaphysics.weebly.com/blog/9795614) |
| WEB-HH-003 | 白虎泄气无拦的住宅 | 实践/问答自述 | 文字；原图未看 | [原来源](https://honghaometaphysics.weebly.com/blog/may-23rd-2021) |
| WEB-HH-004 | 房内猫枕头与睡眠 | 实践/问答自述 | 文字；原图未看 | [原来源](https://honghaometaphysics.weebly.com/blog/9359537) |
| WEB-HH-005 | 顺水局商铺转手 | 实践/问答自述 | 文字；原图未看 | [原来源](https://honghaometaphysics.weebly.com/blog/4344762) |
| WEB-HH-006 | 邻近工地的住宅 | 实践/问答自述 | 文字；原图未看 | [原来源](https://honghaometaphysics.weebly.com/blog/5081384) |
| WEB-HH-007 | 反弓水流住宅 | 实践/问答自述 | 文字；原图未看 | [原来源](https://honghaometaphysics.weebly.com/blog/5183551) |
| WEB-YU-001 | 灶位与参照中心 | 实践/问答自述；隔离 | 文字；原图未看 | [原来源](https://xn--boqti428e.com/) |
| WEB-YU-002 | 暗厅与亮卧室 | 实践/问答自述 | 文字；原图未看 | [原来源](https://xn--boqti428e.com/) |
| WEB-YU-003 | 路口与灶边后门 | 实践/问答自述 | 文字；原图未看 | [原来源](https://xn--boqti428e.com/) |
| WEB-YU-004 | 孩子睡位与文昌 | 实践/问答自述 | 文字；原图未看 | [原来源](https://xn--boqti428e.com/) |
| WEB-YAN-001 | 震宅西北厨房 | 实践/问答自述；隔离 | 文字；原图未看 | [原来源](https://www.yanjunfs.com/M/html/4502363919.html) |
| WEB-YAN-002 | 主卧与婴儿床 | 实践/问答自述；隔离 | 文字；原图未看 | [原来源](https://www.yanjunfs.com/M/html/4502363919.html) |
| WEB-YAN-003 | 办公桌与厕门 | 实践/问答自述；隔离 | 文字；原图未看 | [原来源](https://www.yanjunfs.com/M/html/4502363919.html) |
| WEB-SZ-001 | 住居の風水鑑定と改善の例 | 实践/问答自述 | 文字；原图未看 | [原来源](https://fengshui.jp/archives/468) |
| ED-001 | A Feng Shui harmonization of an irregular-shaped flat | 实践/问答自述 | 文字；原图未看 | [原来源](https://www.fabiopetrella.it/en/a-feng-shui-harmonization-of-an-irregular-shaped-flat/) |
| ED-002 | 北京105平两室改造 | 实践/问答自述 | 文字；原图未看 | [原来源](https://designer.pchouse.com.cn/case/516931_0.html) |
| ED-003 | When a Perfect View Wasn't Enough | 实践/问答自述 | 文字；原图未看 | [原来源](https://www.dezainteria.com/case-study_fengshui) |
| ED-004 | Flying Stars 2026 Singapore Flat teaching case | 教学 | 文字；原图未看 | [原来源](https://www.fengmaster.com/blog/case-study-flying-stars-2026-singapore-flat) |
| ED-005 | 上海115平入口与卧室隐私改造 | 空间参照 | 文字；原图未看 | [原来源](https://designer.pchouse.com.cn/case/515294_0.html) |
| MORE-001 | Case Study – Office Feng Shui | 实践/问答自述 | 文字；原图未看 | [原来源](https://soulspace.info/case-study-office-feng-shui/) |
| MORE-002 | Where's the beef? | 实践/问答自述 | 文字；原图未看 | [原来源](https://www.joeyyap.com/tutorial/tutorial-details.asp?tid=514) |
| MORE-003 | The Manchester Restaurant That Kept Failing — Until the Front Door Was Re-Aligned | 实践/问答自述 | 文字；原图未看 | [原来源](https://danielsiew.com/blog/manchester-restaurant-front-door-feng-shui-story) |
| MORE-004 | Case Study – Feng Shui Design | 实践/问答自述 | 文字；原图未看 | [原来源](https://soulspace.info/case-study-feng-shui-design/) |
| MORE-005 | Design Dilemma (Co Dublin, 2017) | 实践/问答自述 | 文字；原图未看 | [原来源](https://ninakati.ie/authentic-feng-shui-case-study-design-dilemma-co-dublin-2017/) |
| MORE-006 | Before and after of an office – guest room | 实践/问答自述 | 文字；原图未看 | [原来源](https://fengshui-expert.fr/en/before-after-office-guest-room/) |
| MORE-007 | The Benefits of Feng Shui – Case Study Part 2 | 实践/问答自述 | 文字；原图未看 | [原来源](https://masterboon.com/2020/10/08/the-benefits-of-feng-shui-case-study-part-2/) |
| MORE-008 | Master bedroom · sleep | 教学 | 文字；原图未看 | [原来源](https://fengshuiroom.com/cases) |
| MORE-009 | Studio apartment · zoning | 教学 | 文字；原图未看 | [原来源](https://fengshuiroom.com/cases) |
| MORE-010 | 裝修前風水建議案例 — InKiwi Design | 实践/问答自述 | 文字；原图未看 | [原来源](https://hk-fengshui.com/en/case-studies) |
| ROOT-001 | 住宅门前建池与中奖自述 | 实践/问答自述 | 文字；原图未看 | [原来源](https://longyu369.hk/fengshui_case/英格兰阳宅班学员中1万欧元刮刮乐真实案例分享/) |
| ROOT-002 | 总部办公室分区叙述 | 待核 | 文字；原图未看 | [原来源](https://globalfengshui.org/en/research/case/7) |
| HK-001 | 客家建筑研究图 1 | 空间参照 | 原配图已看（范围见记录） | [原来源](https://data.mendeley.com/datasets/xfnynswjfd/1) |
| HK-002 | 客家建筑研究图 2 | 空间参照 | 原配图已看（范围见记录） | [原来源](https://data.mendeley.com/datasets/xfnynswjfd/1) |
| HK-003 | 客家建筑研究图 3 | 空间参照 | 原配图已看（范围见记录） | [原来源](https://data.mendeley.com/datasets/xfnynswjfd/1) |
| HK-004 | 客家建筑研究图 4 | 空间参照 | 原配图已看（范围见记录） | [原来源](https://data.mendeley.com/datasets/xfnynswjfd/1) |
| HK-005 | 客家建筑研究图 5 | 空间参照 | 原配图已看（范围见记录） | [原来源](https://data.mendeley.com/datasets/xfnynswjfd/1) |
| HK-006 | 客家建筑研究图 6 | 空间参照 | 原配图已看（范围见记录） | [原来源](https://data.mendeley.com/datasets/xfnynswjfd/1) |
| HK-007 | 客家建筑研究图 7 | 空间参照 | 原配图已看（范围见记录） | [原来源](https://data.mendeley.com/datasets/xfnynswjfd/1) |
| HK-008 | 客家建筑研究图 8 | 空间参照 | 原配图已看（范围见记录） | [原来源](https://data.mendeley.com/datasets/xfnynswjfd/1) |
| HK-009 | 客家建筑研究图 9 | 空间参照 | 原配图已看（范围见记录） | [原来源](https://data.mendeley.com/datasets/xfnynswjfd/1) |
| HK-010 | 客家建筑研究图 10 | 空间参照 | 原配图已看（范围见记录） | [原来源](https://data.mendeley.com/datasets/xfnynswjfd/1) |
| HK-011 | 客家建筑研究图 11 | 空间参照 | 原配图已看（范围见记录） | [原来源](https://data.mendeley.com/datasets/xfnynswjfd/1) |
| HK-012 | 客家建筑研究图 12 | 空间参照 | 原配图已看（范围见记录） | [原来源](https://data.mendeley.com/datasets/xfnynswjfd/1) |
| HK-013 | 客家建筑研究图 13 | 空间参照 | 原配图已看（范围见记录） | [原来源](https://data.mendeley.com/datasets/xfnynswjfd/1) |
| HK-014 | 客家建筑研究图 14 | 空间参照 | 原配图已看（范围见记录） | [原来源](https://data.mendeley.com/datasets/xfnynswjfd/1) |
| ROUND2-001 | Feng Shui Fertility Case Study February 2019 | 实践/问答自述；暂缓计数 | 文字；原图未看 | [原来源](https://www.loktinfengshui.com.au/feng-shui-fertility-case-study-february-2019/) |
| ROUND2-002 | Fertility Case Study February 2021 Melbourne | 实践/问答自述；暂缓计数 | 文字；原图未看 | [原来源](https://www.loktinfengshui.com.au/feng-shui-fertility-case-study-february-2021/) |
| ROUND2-003 | Case Study – Ana Coppola 2020 | 实践/问答自述；暂缓计数 | 文字；原图未看 | [原来源](https://www.loktinfengshui.com.au/case-study-ana-coppola-2020/) |
| ROUND2-004 | Yin Feng Shui Case study from China | 译述实践 | 文字；原图未看 | [原来源](https://www.loktinfengshui.com.au/yin-feng-shui-case-study-from-china-provided-by-a-feng-shui-fellow-student/) |
| ROUND2-005 | Feng Shui Warehouse | 实践/问答自述 | 文字；原图未看 | [原来源](https://www.loktinfengshui.com.au/feng-shui-warehouse/) |
| ROUND2-006 | Feng Shui Fertility Baby | 实践/问答自述 | 文字；原图未看 | [原来源](https://www.loktinfengshui.com.au/feng-shui-articles/feng-shui-fertility-case/) |
| ROUND2-007 | Feng Shui Staircase Design — Macau church example | 教学 | 原配图已看（范围见记录） | [原来源](https://www.loktinfengshui.com.au/feng-shui-staircase/) |
| ROUND2-008 | Feng Shui Staircase Design — Summer Palace example | 教学 | 原配图已看（范围见记录） | [原来源](https://www.loktinfengshui.com.au/feng-shui-staircase/) |
| ROUND2-009 | The Block That Looked Perfect — But Traps You Inside | 实践/问答自述 | 文字；原图未看 | [原来源](https://www.ifengshui.sg/insights/the-block-that-looked-perfect-but-traps-you-inside/) |
| ROUND2-010 | Office CEO room selection — step-by-step example | 教学 | 文字；原图未看 | [原来源](https://www.geomancy.net/forums/topic/17969-is-a-squarish-or-narrow-layout-better-for-an-office-unit-what-key-factors-should-i-consider-does-this-also-apply-to-homes/) |
| ROUND2-011 | Farrer Park Arena stack ranking case | 实践/问答自述 | 文字；原图未看 | [原来源](https://www.geomancy.net/forums/topic/20989-when-feng-shui-advice-goes-wrong-how-a-master-can-misread-your-home-ranking-choice/) |
| ROUND2-012 | Living-room furniture and main-door route — Case Study 9 | 实践/问答自述 | 文字；原图未看 | [原来源](https://www.geomancy.net/forums/topic/17949-volume-1-of-2-selected-cases-with-real-life-examples-of-ba-zi-feng-shui-eight-house-flying-stars-shapes-forms-water-classics-lots-more-concepts-useful-to-get-into-the-head-of-a-fs-master/) |
| ROUND2-CN-001 | 新婚卧室风水摆放位置？ | 实践/问答自述 | 文字；原图未看 | [原来源](https://cn.cari.com.my/forum.php?mod=viewthread&tid=3507505) |
| ROUND2-CN-002 | 请帮忙看看房子风水 | 实践/问答自述 | 文字；原图未看 | [原来源](https://cn.cari.com.my/forum.php?mod=viewthread&tid=3781571) |

## 客家建筑图与署名


此前研读图1–7与图8–14两张联系表；当前发行包不含联系表图像，仅保留原数据链接及历史阅读记录。数据发布者 nannan Qu，*Research on the Spatial Configuration and Layout of Chinese Hakka Architecture Based on the CNN-LSTM-Attention Method*，2026，版本1，DOI 10.17632/xfnynswjfd.1；[原数据](https://data.mendeley.com/datasets/xfnynswjfd/1)，发布许可 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。联系表将原上传图截图缩小、拼接并加编号，本项目未校改底图。

仅看联系表中可辨图形，细小题记未逐字辨认。源中的九方向、126数据点和匹配分数不增加案例数，也不是吉凶/健康标签。原压缩包27,039,574字节，SHA-256为563017f0fab38c53655678b2ac6ec884a23ad00e0f4ff24536c885c390c53ab2，已核验；压缩包与模型文件不随技能分发，也未执行其中的模型。


## 来源访问记录与现有资料的使用

本轮进一步核查中文与英文公开来源，见[来源可用性](source-availability.md)和[source-audit.json](source-audit.json)。佳礼及Geomancy有万级主题候选数，但版内混有泛论、重复项目或其他术数，目录数不是已研读案例数；两站统计也不能直接相加成独立住宅数。Geomancy版权告示限制复制、存储与改编，不能据公开阅读推定批量语料许可。

龙行天下普通HTTP和内置浏览器曾出现502，此处保留访问记录。查资料时从[既有来源入口](recorded-sources.md)按主题选读，把真正读到的格局、取法与差异用于知识补充；不为了本地笔记数量重复处理案例或照片。论文研究样本、普通户型和九宫数据点分别解释，不能互换成咨询实录。
