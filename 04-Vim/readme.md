# VIM
VIM是最基本，也是最重要的命令行编辑器。而且操作和常规的文本编辑器完全不一样，需要特别的学习
基本概念：
- 模式
	- command
	- insert
	- last line
- 各种模式的快捷键
	- cursor movement
	- insert mode
	- editing mode
	- exiting mode
	- search
	- visual mode
	- cut and paste - windows operation 
## 模式
刚进入VIM是处于`command mode`,需要按下`i`进入`insert mode`才能编辑
通过观察promote的最下面一行，可以知道自己位于哪种模式
- `--INSERT--`:按下`i`
- 空白：command模式。按下`Esc`

### command
命令模式只有一些最基本的命令，因此仍要依靠底线命令模式输入更多命令。
- i 切换到插入模式，以输入字符。
- x 删除当前光标所在处的字符。
- : 切换到底线命令模式，以在最底一行输入命令。
### last line
都要先输入：，以下的命令省略了：
- q！ 不保存，强制退出
- w！ 强制保存，不退出 
- wq！ 强制保存，并且推出 
## shortcut 
### cursor movement
在command模式下
- ctrl+f 上一页
- ctrl+b 下一页
- w e 下一个单词
- b 上一个单词
- o 插入新的一行
- ^ 一行的开始
- $ 一行的结束
- gg 文档第一行
- [N]G 文档最后一行，或者第N行


### 不同的插入位置
- i 插入到光标前面
- I 插入到行的开始位置
- A 插入到行的最后位置
- o, O 新开一行
- Esc 关闭插入模式

### Editing
- S 删除光标所在的一行，光标还在当行，不同于dd
- u 撤销上一步操作
- ctrl+r 恢复上一步操作
- . 重复最后一个命令
- V 选中一行

### 剪切和复制
- dd 删除一行
- [N]yy 复制一行
- p 粘贴




