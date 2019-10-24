# 习惯清单


## 快速开始

* 


## 创作过程

* (可以直接先small hack一下)
* 在纸上模拟逻辑，搞清楚逻辑，后面会顺畅许多
* 翻译成伪码
* 写成代码
* 删掉伪码，看看代码如何优化（发现其中的模式并提炼简化）
* 

## 审核代码

* 模拟自己是计算机
* 从unit_test的第一行代码开始，一行一行运行，进入function和logic branch
* 清楚自己运行的assumption是什么（类型/内容...)，预计输出是什么。
* 在必要的地方加入assert确保你的assumption符合实际情况（不推荐，因为test应该面向interface。但必要时可以使用）
* 如有必要可以在主程序中加入assert（特别是在逻辑branch中）
* 思考是否所以case都在test中考虑到了？（有没有遗漏？）
* 如何还有bug，使用print的办法（pytest -s）


## 其他

* 用pyshell快速确认api等
* 使用count代替n(更好读)
* debug用的print(">>> xxx: ", xxx)更显眼
* 写完function后写unit_test，然后audit代码。不要等到全部写完再audit
* 碰到单独的问题，可以分离成单独的function并单独test
* _invariable思想：确保每次都符合一组assumption（否则可能难以发现问题出在哪里）
* 写block的时候，可以快速先把结构和简单的地方填入
* 边界/if问题，可以上来先用笨办法列举，然后再合并