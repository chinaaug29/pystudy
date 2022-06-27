---
title: git基础 
CreatedTime: 2022-06-25 11:00
UID: 20220625110617
priority: #优先级,分4级：4重要紧急，3紧急，2重要，1不重要不紧急
所属项目: 
类型: 
状态: 
tags: [git] #标签
aliases:  #别名
  - git初始命令
  -
  -
---
## 获取git仓库

- 从其它服务器 克隆 一个已存在的 Git 仓库
  - `git clone https://github.com/libgit2/libgit2`网址可以更换为自己需要克隆的仓库地址
- 在已存在目录中初始化仓库
 1. `cd /c/user/my_project` # 进入需要创建git的目录
 2. `git  init` # 初始化目录，该命令将创建一个名为 .git 的子目录，这个子目录含有你初始化的 Git 仓库中所有的必须文件，这些文件是Git 仓库的骨干。

```git
git add *.c  # 指定需要跟踪的文件
git add LICENSE   # 跟踪文件并放入暂存区
git commit -m 'initial project version' # 提交更新文件到仓库，并撰写提交信息，提交信息是必须的，如果留空，提交到仓库的动作就终止。
```

>工作目录下的每一个文件都不外乎这两种状态：已跟踪 或 未跟踪。
>已跟踪的文件是指那些被纳入了版本控制的文件，在上一次快照中有它们的记录，在工作一段时间后， 它们的状态可能是未修改，已修改或已放入暂存区。简而言之，已跟踪的文件就是 Git 已经知道的文件。
>工作目录中除已跟踪文件外的其它所有文件都属于未跟踪文件，它们既不存在于上次快照的记录中，也没有被放入暂存区

- 检查当前文件状态
  - `git status`  # 查看哪些文件处于什么状态

```
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed: # 要提交的更改
(use "git reset HEAD <file>..." to unstage)
 new file: README 
Changes not staged for commit:  # 更改没有暂存以便提交
(use "git add <file>..." to update what will be committed)
(use "git checkout -- <file>..." to discard changes in working
directory)
 modified: CONTRIBUTING.md
```

- 这时运行`git add CONTRIBUTING.md`命令将CONTRIBUTING.md文件放到暂存区
