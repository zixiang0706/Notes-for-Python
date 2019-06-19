# Git

## 链接dev和origin/dev

## gitignore

## use case



1. 修改了文件，已经add了，删除add`git reset .`
2. 丢弃修改`git checkout .`
3. 回复到最新一次的HEAD`git reset HEAD`
4. 回复到指定的head`git checkout [headID]`
5. 软硬复位head
   - `git reset --hard [HASH] ` 有可能会丢失head
   - `git reset --soft [HASH] `
6. 把内容存到stash
   - `git stash `
   - `git stash pop`恢复stash
7. 查看所有分支`git branch -a`
8. 删除本地分支`git branch -D dev2`
9. 删除远程分支`git push origin --delete dev2`

# Pycharm+Git

## 底部菜单栏 Log

1. checkout revision可以把head 指定到这个位置，效果和checkout一致

![img](assets/img.png)

2. 注意solve conflict的方式。
   - 一般来说，选择force也可以
   - accept theirs：选择老的
   - accept yours： 选择新的
3. 

