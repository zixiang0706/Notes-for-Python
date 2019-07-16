# VIM
详细的介绍可以[参考这个网址](https://lxs647.iteye.com/blog/1245948)

VIM的三种模式是核心：
1. command line (normal mode)
2. insert mode
3. last line

## 基本介绍
刚进入VIM是处于`command mode`,需要按下`i`进入`insert mode`才能编辑
通过观察ssh的最下面一行，可以知道自己位于哪种模式:

1. 显示`--INSERT--`，处于insert-mode， 按下`Esc`进入command-mode
2. 空白，或者显示键盘的输入，处于command-mode 或者last-line-mode， 按下`i/o/a`进入insert-mode

## command (normal)
命令模式只有一些最基本的命令，因此仍要依靠底线命令模式输入更多命令。但是基本功能又是最常用的。
- x 删除当前字符
- da 删除当前单词
- u 撤销一步
- yy 复制一行
- [n]yy 复制n行
- dd 删除一行
- [n]dd 删除n行
- dG 后面的全删 

### 行操作
- ctrl+f 上一页
- ctrl+b 下一页
- w e 下一个单词
- 光标去行首^
- 光标去行尾$

### 定位
- gg 首行
- G 尾行
- 2gg 第二行 
- [N]G 文档最后一行，或者第N行

### Enter insert
- i 插入，光标位置
- I 插入，到行首
- A 插入到行的最后位置
- o 新开一行,插入到当前行之后
- O 新开一行,插入到当前行之前


## search
1. `/[word]`
2. `enter`
3. n，显示下一个;N, 显示上一个 

## visual block
用来批量添加/删除注释 
###添加
1. ctr+v,进入visual block
2. 用箭头选中多行
3. 输入I，输入#
4. 按2次esc
###删除
1. 再command模式下,ctr+v,进入visual 模式
2. 用箭头选中多行
3. 按下d，就会删除对应字符

## last-line
都要先输入：，以下的命令省略了：
- ：开启模式
- w 写入
- q 退出，不保存
- ！ 强制模式
- wq！ 写入，并且强制退出
- `![command]` 会在shell调用这个command，如:!date
- `%s/3/4/g` 全部替换
- `set nu` 显示行号
- `set nonu` 不现实行号




