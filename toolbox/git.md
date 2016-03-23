一.安装GIT和配置GIT

1.安装GIT
$ apt-get install git

2.配置GIT

# 配置用户信息
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com

# 设置别名
git config --global alias.ci commit
git config --global alias.st status

# 编辑器
$ git config --global core.editor vim

# 差异分析工具
$ git config --global merge.tool vimdiff

# 颜色显示
$ git config --global color.ui true

# 独立忽略文件
$ git config --global core.excludesfile /home/linzhenjie/.gitignore

# 查看配置信息
$ git config --list

# 获取帮助
$ git help config


二、创建GIT仓库和远程仓库的使用

1.在工作目录中初始化新仓库
$ git init

2.从现有仓库克隆出来
$ git clone git://192.168.1.1/var/www/test.git

3.克隆到本地
$ git clone /var/www/test test_new

4.远程仓库的克隆
$ git clone root@192.168.1.1:/var/www/test

5.查看当前的远程库
$ git remote -v

6.添加远程仓库和推送

# 添加远程仓库分支
$ git remote add test root@192.168.1.1:/var/www/test
# 从远程仓库抓取数据
$ git fetch test
# 推送数据到远程仓库
$ git push origin master
# 查看远程仓库信息
$ git remote show origin

7.远程仓库的删除和重命名

# 重命名
$ git remote rename test test_new
# 删除
$ git remote rm paul


三、GIT中相关命令

1.检查当前文件状态
$ git status
$ git status -s

2.往暂存库中添加新的文件
$ git add test.php
$ git add -A

3.提交更新

# 提交更新
$ git commit -m "message"
# 添加并提交更新
$ git commit -a -m 'message'
# 执行一次空白提交
$ git commit --allow-empty -m "who does commit?"

4.branch分支

#  列出分支
$ git branch
# 列出远程分支
$ git branch -a
# 创建新分支
$ git branch branch-name
# 将新建分支push到远端
$ git push origin <branch-name>
# 拉取远端分支
$ git pull origin <branch-name>

# 删除分支
$ git branch -d branch-name
# 删除远程分支
$ git push origin --delete <branch-name>
$ git push origin :<branchName>  # 推送一个空分支到远程分支==删除
# 创建新分支，并立即切换到它
$ git checkout -b branch-name

# 切换分支
$ git checkout master
$ git checkout branch-name
$ git checkout branch-name -- filename # 将xxx分支的xxx文件替换当前分支的文件,解决冲突时有用.

# 将分支合并到当前的分支
$ git merge branch-name

# 设置本地分支和远端分支的对应跟踪
$ git branch <branch-name>  切换到对应分支
$ git branch --set-upstream-to=origin/<branch-name>

5.比较差异

# 暂存库与版本库比较
$ git diff
# 本地库与暂存库比较
$ git diff HEAD
# 暂存库与版本库比较
$ git diff --cached
$ git diff --staged

# 冲突标记
<<<<<<<HEAD
当前分支内容
=======
合并过来的分支的内容
>>>>>>>6853e5ff96.........

6.修改最后一次提交

$ git commit -m 'initial commit'
$ git add test.php
$ git commit --amend

7. 查看提交历史

# 查看所有日志
$ git log
# 查看所有日志(包含重置的日志)
$ git reflog show master
# 查看某个文件某次的修改
$ git show <某次提交的哈希值> 文件名
# 查看那几个文件改变了
$ git whatchanged

8.重置/回退暂存区和版本库

# 回退未提交的修改
$ git checkout .
# 重置/回退版本库
$ git reset --soft 
# 重置/回退版本库、暂存库
$ git reset
# 重置/回退版本库、暂存区、工作区
$ git reset --hard

9.清理工作区

# 查看不在暂存区的工作区文件
$ git clean -nd
# 清理工作区多余文件
$ git clean –fd

10.删除暂存区和版本库

# 删除暂存库和版本库的文件
$ git rm test.php
# 删除版本库的文件
$ git rm --cached test.php

11.移动文件

$ git mv test.php test_new.php

12.进度的存储和恢复

# 保存当前进度
$ git stash save
# 查看当前进度列表
$ git stash list
# 弹出恢复工作区进度
$ git stash pop
# 弹出恢复工作区和暂存区进度
$ git stash pop --index
# 应用工作区进度
$ git stash apply
# 删除一个进度
$ git stash drop
# 删除所有存储进度
$ git stash clear
# 存储分支进度
$ git stash branch

13.软件发布时创建标签

# 查看标记
$ git tag

# 将提交ID为“1b2e1d63ff.....”的提交标记为v1.0.0
$ git tag v1.0.0 1b2e1d63ff

#  将最新提交打上“v1.0”的标签
$ git tag -a v1.0


四、忽略文件语法

.gitignore
*.a            # 忽略以.a为节结尾的文件
!lib.a         # 不会忽略lib.a的文件或目录
/DIR           # 忽略当前目录下文件（不包括子目录）
DIR/           # 忽略当前目录下所有文件
DIR/*.txt      # 忽略DIR下的txt文件（不包括子目录）

五、同步github的原作者
$ git remote -v 查看远端仓库
$ git remote add upstream https://github.com/xxxxx/xxxxx.git
$ git remote -v
$ git fetch upstream
$ git checkout master
$ git merge upstream/master

六、常用
$ git remote prune origin   # remote上的一个分支被其他人删除后，需要更新本地的分支列表 