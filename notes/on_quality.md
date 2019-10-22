# Quality

> understand what's good

Zed认为，质量问题的来源之一是对自己的代码太熟悉，以至于忽视了某些缺陷和细节。

代码能跑之后要做更多事情

> there’s a mountain of work to do after that, from cleaning the code up, performing quality assurance checks, adding invariants and assertions, writing tests, writing documentation, and confirming it works within the larger context of the whole system.

虽然完全清除bug不太可能，但通过清单检查可以把概率大大降低。

Zed对quality的定义：

> A low defect rate and understandable code

## 质量清单

* 建立客观质量指标
* 自动测试
* 对于固定的数据结构/模式，为此集中写一个test(_invariants)

## 任务

把你发现自己的bug统计下，并分类汇总。

一种分类思路：

* 逻辑链错误
* 数据类型错误
* 调用函数错误