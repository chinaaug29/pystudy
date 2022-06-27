
git报错:‘origin‘does not appear to be a git repository的解决方法

# 事故现场

git push origin master时报错：

fatal: 'origin' does not appear to be a git repository


# 解决方法

使用`git remote -v`命令，什么都没有输出；
说明和远程已失去联系，这种情况可能是远程仓库已改名，或者是git remote add时操作没有将相关配置加上（或者有异常）；
第一种可能可以排除，那就是第二种可能了。

和其他git项目对比了一下.git/config文件，发现了问题所在，这个git仓库只有[core]节点，没有[remote “origin”]和[branch “master”]节点信息。

```
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
```

也就是说当你git push origin master的时候，git需要去config中查找你提交的分支信息，但是config中又是空的，所以返回上述错误。
所以解决方法就是把信息直接填上：

```
[core]
 repositoryformatversion = 0
 filemode = false
 bare = false
 logallrefupdates = true
 symlinks = false
 ignorecase = true
[remote "origin"]
 url = <http://192.168.1.183/git/RCTools.git>
 fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
 remote = origin
 merge = refs/heads/master
```

