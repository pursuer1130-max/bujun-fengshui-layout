# 十万既有风水案例：本轮来源核查

核查日期：2026-10-30。已先读现有 `recorded-sources.md`、`corpus-progress.md`、`research-samples.json`，未重复打开此前多次失败的论坛。目标按用户最新要求保留为**不少于100,000个已有记载的风水案例**，不能替换成制作100,000份照片报告。

**本轮未找到能够支持目标规模的可读独立风水原案集合，也未完成十万案例研读。** 新取得的原案全文为0；本轮工作是核数量单位、来源性质与正文可达性，不是把目录条目算作已读原案。此结论只涵盖本轮候选，不是断言网上不存在此类资料。

## 已核新候选

| 来源 | 直接读取的证据 | 为什么不计入十万原案 |
|---|---|---|
| [AmareshHebbar/nine_star_ki-sft](https://huggingface.co/datasets/AmareshHebbar/nine_star_ki-sft) | 卡片声明100,000行、Apache 2.0；限制节明确全为合成资料，且未实现方位/风水应用 | 是九星气学的合成训练行，不是真实阳宅/阴宅原案；未下载28.6MB数据 |
| [jakeveo05/tcm-divination-training](https://huggingface.co/datasets/jakeveo05/tcm-divination-training) | Viewer显示215k行；卡片声明CC BY 4.0，来源表含八字书OCR、GPT问答及占星/塔罗等 | 混合训练集；48,551项明确是GPT生成问答，其他OCR、问题行亦不能直接换成风水项目。只核卡片和样例，未下载全量 |
| [zwh20081/houselayout viewer](https://huggingface.co/datasets/zwh20081/houselayout/viewer/default/train) | Viewer显示1.76k行；检索样例为工厂选址与一般风水知识问答 | 未见逐项目原载、现场关系及咨询身份。卡片打开失败、许可未核；不把文件名houselayout当户型原案证据 |
| [Conard/fortune-telling](https://huggingface.co/datasets/Conard/fortune-telling) | 207行、MIT标注；Viewer含Question/Response/Complex_CoT，混有八字、紫微、塔罗与泛风水问题 | 未见可追溯独立住宅/墓地项目记录；不因模型被称“风水大师”就把其训练集当原案。与既有同规模镜像关系未核，不重复计数 |
| [Feng Shui Society案例页](https://www.fengshuisociety.org.uk/feng-shui-case-studies/) | 页面宣称有许多案例，但本次正文两处显示No Results Found；另可读报告提交指导 | 不是当前可读的逐案集合，指导不是案例；不把countless换成数字 |
| [Global Feng Shui Association实践案例目录](https://globalfengshui.org/en/research/all-cases.asp) | 直接读到6个项目卡片，包含易经策略等不同主题；详情、去识别案例、年度数据链接打开均失败 | 6为当前目录卡片数，不能当6份已读原案或全站总量；机构身份和项目事实未另核 |
| [新西兰风水学院FAQ](https://fengshuimasteryou.wixsite.com/fengshuinewzealand/faq)及[旧案例栏目](https://fengshuimasteryou.wixsite.com/fengshuinewzealand/blog) | FAQ将“建立最大案例数据库”写为宗旨；栏目首页有5页入口，混有新闻事后解释、命理及风水 | 宗旨不等于已有规模；未见总量或数据集。与现有Master You来源有关，不推定独立新增库 |
| [Kartar Diamond Case Study Club](https://fengshuisolutions.net/feng-shui-case-study-club/) | 公开说明为进阶教学系列，含题名与简介，全文为收费下载 | 可定位坐向、小空间、分层飞星等教学题目；未购买/未读全文，不把回答数千问题换成数千独立案例 |
| [iFengShui Insights](https://www.ifengshui.sg/insights/) | 首页“thousands of audits”为执业经验说法；stories详情入口本次cache miss | 未见同规模公开逐案目录，不按营销经验数报已取得资料 |

没有对上述来源作批量抓取、购买、注册或联系作者；现代内容只保存元数据、链接和短原创核查笔记。机器记录见 `[来源记录](hundredk-sources.json)`。

## 对当前skill的实际影响

保留十万目标，但进度仍依“可追溯原案、实际读取范围、同案归组”登记。新增阴宅与阳宅功能可以通过确实读到的书籍篇章和少量真实案例改善，不能因功能已更新便把数量目标标为完成。研究样本、书稿切片、教学题名、命理命盘和合成训练行继续分别记单位。

用户进一步要求直接查书后，已转向《阳宅十书》《阳宅三要》《雪心赋》的公版/机构版入口与指定篇章；实际范围见 `book-source-checks.md`。书目、影印元数据、转录正文及已校影印是不同状态，均不增加案例数。
