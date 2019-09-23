[TOC]

# Git

## basic knowledge`

1. branch
   1. master: the main branch, main repo
   2. Origin: the remote branch
   3. Create and switch to a new branch: 	`git checkout -b dev`
   4. 查看所有分支`git branch -a`
   5. 删除本地分支`git branch -D dev2`
   6. 删除远程分支`git push origin --delete dev2`
2. merge
   1. when the brach have diff commit, means it has diverge, it cannot ff
   2. fast forward：`git merge dev`
   3. No ff: `git merge --no-ff -m 'no ff' dev`
3. stash
   1. stash: `git stash `
   2. Show the stash list: `git stash list`
   3. recovery stash: `git stash pop`
4. log
   1. 查看历史版本 `git log`
   2. 查看简短的历史版本: `git log --pretty=oneline`
   3. log with graph: `git log --graph --pretty=oneline`
   4. 查看历史操作`git reflog`
5. version
   1. This version : HEAD
   2. lasr version: HEAD^ HEAD~1
6. diff
   1. 查看和当前的修改差异：`git diff HEAD -- <file>`
   2. 查看两个版本之间的修改差异：`git diff HEAD^ HEAD -- <file>`

## 链接dev和origin/dev

`git remote add origin https://github.com/zixiang0706/Digital-Figure-Reco.git`

`git push -u origin master`
`git push --set-upstream origin master --force`

## gitignore

## use case

1. 丢弃工作区：
   1. `git checkout .`
   2. git checkout <headID>
2. 丢弃暂存区：
   1. `git reset .`
   2. `git reset <headID>`
3. 软硬复位head
   - `git reset --hard [HASH] ` 有可能会丢失head
   - `git reset --hard HEAD~`回到上一个版本
   - `git reset --soft [HASH] `
4. 最新提交合并到上一个commit `git commit --amend`
5. force push  `git push -f`

# Pycharm+Git

## 底部菜单栏 Log

1. checkout revision可以把head 指定到这个位置，效果和checkout一致

![img](assets/img.png)

2. 注意solve conflict的方式。
   - 一般来说，选择force也可以
   - accept theirs：选择老的
   - accept yours： 选择新的
3. 
生成requirements：`pipreqs --force ./ --encoding==utf8`

