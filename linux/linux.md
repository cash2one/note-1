####常用
```bash
$ command --help  => 查看command的帮助
$ info command    => 查看command的信息
$ man command     => command 手册
$ which  command  =>  查看命令的完整路径
  
ctrl + H     =>  显示隐藏文件
ctrl + z     =>  暂停进程转到后台
ctrl + c     =>  停止
ctrl + A     =>  光标称动到开头
ctrl + E     =>  光标移动结尾
ctrl + W     =>  回退一个单词
ctrl + d     =>  exit
  
$ man ascii       => ascii码表
  
$ sudo apt-get update
$ sudo apt-get upgrade
$ apt-cache search package-name   => apt搜索包
$ sudo apt-get remove --purge package-name   => 连同配置信息一起卸载
  
$ sudo nautilus     => 以root权限打开一个窗口, 来管理文件
$ sudo      => 以系统管理者的身份执行指令
$ top       => 资源管理
$ reboot    => 重启机
$ shutdown  => 关机
    shutdown -h now  # 现在关机
    shutdown -h hours:minutes  # 按预定时间关闭系统
    shutdown -c  # 取消按预定时间关闭系统
    shutdown -r now  # 重启计算机, 停止服务后重新启动计算机
  
$ login
$ logout
$ passwd
  
$ uname -r  => 查看内核版本
  
$ w       => 显示登录用户的详细信息
$ who     => 显示登录用户
$ whoami  => 查看当前登陆的用户名 
$ last    => 查看最近哪些用户登录系统
$ su    => 变更使用者身份
    su root
    su username  # 切换用户
  
$ lscpu   => 查看cpu统计信息
$ free    => 查看内存情况
    free -m  # -m 单位MB
$ vmstat  => 监视虚拟内存使用情况
  
$ export  => 查看所有环境变量
$ env     => 查看所有环境变量
$ echo $PATH  => 查看环境变量PATH
$ export HELLO='hello'  => 设置变量HELLO, 这是临时的变量, 在关闭shell时失效
  
$ date    =>  显示日期
$ uptime  =>  现在时间, 系统开机运转到现在经过的时间, 连线的使用者数量, 最近的系统负载.
$ cal     =>  显示一个日历
$ bc      =>  一个简单计算器
```

#### 环境变量
```
* 在/etc/profile文件中添加变量, 对所有用户生效
  
* 用户目录下的.bash 和 .profile文件中增加变量, 对单一用户生效
  
* (ubuntu下为home目录下的.bashrc和.profile, /etc/profile; /etc/evnironment)
  
* export PATH=/opt/node/bin:$PATH
  
* (/etc/environment不需要使用export设置环境变量, 其他profile文件需要)
  
* source ~/.bashrc  使新变量立即生效
```

#### 用户, 组, 权限
```
linux用户主要分为三类:
* root(超级管理员), UID为0, 这个用户有极大的权限, 可以直接无视很多的限制, 包括读写执行的权限.
* 系统用户, UID为1~499. 一般是不会被登入的.
* 就是普通用户, UID为500~65534. 这类用户的权限会受到基本权限的限制, 也会受到来自管理员的限制.
   不过要注意nobody这个特殊的帐号, UID为65534, 这个用户的权限会进一步的受到限制, 一般用于实现来宾帐号.
  
/etc/group   # 文件包含所有组
/etc/passwd  # 用户(user)的配置文件
例: baixue:x:1000:1000:baixue,,,:/home/baixue:/bin/bash
用户名:口令:UID:GID:用户描述:home目录:用户使用的shell
  
密码项中: x 表示密码经过加密放到/etc/shadow文件中了
  		  * 表示该账号被查封了，系统不允许持有该账号的用户登录
shell项中: /usr/sbin/nologin 表示账号无法登录
           /bin/false 不给该用户正常的SHELL，不允许该用户登录
  
/etc/shadow  # 用户user影子口令文件
/etc/sudoers # sudo用户配置
  
$ useradd/adduser  => 添加用户
	# 一般用useradd即可, adduser会交互式的提示你创建用户信息
    useradd -d /usr/sam -m sam -g sam  # -d 用户home目录, -m 用户名 -g 组
  
$ usermod  => 修改用户
	例:
	usermod user -aG groups1,group2,group3  # 将user用户添加到group1, group2和group3组中
  
$ userdel  => 删除用户
    userdel -r sam  
    # 删除用户sam在系统文件(主要是/etc/passwd; /etc/shadow; /etc/group等)中的记录, 同时删除用户的主目录.
  
$ passwd  # 修改密码
  
$ groupadd/addgroup
  
$ groupmod
  
$ groupdel
  
$ groups
  
$ id username  => 显示用户信息
  
$ chown  =>  改变目录的用户和组 
  
$ chmod 
    三种基本权限
    R: 读      数值表示为4
    W: 写      数值表示为2
    X: 可执行  数值表示为1

    chmod abc file
    r=4, w=2, x=1
    其中a,b,c各为一个数字，分别表示User、Group、及Other的权限
    若要rwx属性则4+2+1=7
    若要rw-属性则4+2=6
    若要rx-属性则4+1=5

    例: chmod a=rwx file 和 chmod 777 file

$ sudo chmod +x nginx  # 添加可执行权限
$ sudo chmod -x nginx  # 取消可执行权限
$ sudo chmod +w file   # 添加可写权限
$ sudo chmod -w file   # 取消可写权限
$ sudo chmod +s /bin/netstat   # 让用户免root运行

  
$ lsblk    => 查看硬盘和分区分布
  
$ sudo fdisk -l    => 查看硬盘和分区的详细信息
  
$ df -h   =>  显示已挂载的分区列表
  
$ mount    => 挂载磁盘分区
$ mount -o remount, rw / (recovery mode 时，重新过载根分区为可读写
$ umount   => 卸载磁盘分区
    mount /dev/sda5 /mnt/d  # /mnt目录下要有d这个目录
    umount /dev/sda5
  
$ gcc
    gcc -o test test.c
```

#### 常用
```
$ cd
    cd ..     # 返回上级目录
    cd ../..  # 返回上两级目录
    cd /      # 进入根目录
    cd -      # 返回上次的目录
    cd        # 进入个人主目录
    ~         # 代表/home/用户名目录
    cd ~/.local  # 表示用户主目录下有个.local的目录，"."表示这是个隐藏文件
  
$ ll -h           => 大小易读,有单位
$ cat filename    => 查看文件
$ stat filename   => 查看文件状态
$ more filename   => 分页查看 space下一页, b上一页

    ps ux|more
    ls|more
  
$ nl filename   => 带行号查看文件
$ file          => 查看文件类型
  
$ wc            => 统计文本中函数、字数、字符数
$ grep          => 在指定文件中搜索特定内容--Global Regular Expression

    grep [OPTIONS] PATTERN [FILE...]
    grep [OPTIONS] [-e PATTERN | -f FILE] [FILE...]
	grep -r re -n  # 在当前文件夹中搜索包含该re的文件
  
$ diff          => 分析两个文件的不同

    diff dir1 dir2    # 比较目录1和目录2的文件列表是否相同,不比较文件，不同则列出
    diff file2 file2  # 比较文件
    comm file1 file2  # 比较文件，显示不同的内容
  
$ patch         => 应用补丁
  
$ pwd           => 显示工作目录完整路径
  
$ ln            => 建立链接

    ln source_path target_path     # 硬链接
    ln -s source_path target_path  # 软链接
  
$ du            =>    显示目录或文件的大小

    -b: 以byte为单位
    -h: 以K，M，G为单位
    -m: 以M为单位
	例: du -sh * 查看当前目录第一级各个目录的大小
	    du -sh 显示当前目录的大小
  
$ tree          =>  显示目录树

    $ tree -D -L 1
    -d:只显示目录
    -L:选择显示的目录深度
    1：只显示一层深度，即不递归子目录
  
$ mkdir 目录名     => 创建一个目录

    mkdir name1 name2...
  
$ rmdir 空目录名   => 删除一个空目录

    rm -rf 目录名  # 删除非空目录
  
$ ls   => 列出目录下的文件

    ls -l  # 显示文件和目录的详细信息($ ll)
    ls -a  # 显示隐藏文件($ la)
    ls -d */  # 只显示目录
    ls -l | grep ^d  # 只显示目录
	ls -l | grep ^-  # 只显示文件a
  
$ find    => man find
	常用简化形式:
	find [path...] [expression]
	path: find命令所查找的目录路径, 例: 用.来表示当前目录, 用/来表示系统根目录
	expression: expression可以分为——"-options [-print -exec -ok ...]"
	-options  指定find命令的常用选项
	-print  find命令将匹配的文件输出到标准输出
	-exec  find命令对匹配的文件执行该参数所给出的shell命令.相应命令的形式为'command' {} \; 注意{}和\;之间的空格
  
# 统计代码行数
$ find . -name "*.py" | xargs wc -l
$ find . -name "*.py" | xargs cat|grep -v ^$|wc -l  # 去除空行
  
# 删除文件大小为零的文件
$ find ./ -size 0 -exec rm {} \; 或 rm -i 'find ./ -size 0'
  
# 删除目录及其子目录下某类型的文件
$ find . -name "*.txt" -delete
$ find . -name "*.pyc" -type f -print -exec rm -rf {} \;
    .  # 表示在当前目录下,可以省略，默认就是当前目录
    -name "*.txt"  # 表示查找所有后缀为txt的文件
    -type f  # 表示文件类型为一般正规文件
    -print  # 表示将查询结果打印到屏幕上
    -exec command  # command为其他命令,-exec后可再接其他的命令来处理查找到的结果,{}表示由find命令查找到的结果
  
# 删除除了某类型的文件外的所有文件
$ find . -type f -not \( -name '*.zip' -or -name '*.iso' \) -delete
  
# 为了用ls -l命令列出所匹配到的文件，可以把ls -l命令放在find命令的-exec选项中
$ find . -type f -exec ls -l {} \;
  
# 在/logs目录中查找更改时间在5日以前的文件并删除它们
$ find /logs -type f -mtime +5 -exec rm {} \;
	-ok和-exec的作用相同,只不过以一种更为安全的模式来执行该参数所给出的shell命令,在执行每一个命令之前,都会给出提示,让用户来确定是否执行.
# 在当前目录中查找所有文件名以.LOG结尾,更改时间在5日以上的文件,并删除它们,只不过在删除之前先给出提示
$ find . -name "*.conf"  -mtime +5 -ok rm {} \;
  
# find命令的常用选项及实例
	-name 按照文件名查找文件
		# 在/dir目录及其子目录下面查找名字为filename的文件
		$ find /dir -name filename
		# 在当前目录及其子目录（用"."表示）中查找任何扩展名为"c"的文件
		$ find . -name "*.c"

	-perm 按照文件权限来查找文件
		# 在当前目录下查找文件权限位为755的文件
		$ find . -perm 755 –print

	-prune 
		# 在/apps目录下查找文件，但不希望在/apps/bin目录下查找
		$ find /apps -path "/apps/bin" -prune -o –print 
		# 在/usr/sam目录下查找不在dir1子目录之内的所有文件
		$ find /usr/sam -path "/usr/sam/dir1" -prune -o –print

	-user 按照文件属主来查找文件
		# 在$HOME目录中查找文件属主为sam的文件
		$ find ~ -user sam –print

	-type 查找某一类型的文件
		b - 块设备文件
		d - 目录
		c - 字符设备文件
		p - 管道文件
		l - 符号链接文件
		f - 普通文件
		# 在/etc目录下查找所有的目录
		$ find /etc -type d –print
		# 在当前目录下查找除目录以外的所有类型的文件
		$ find . ! -type d –print
  
$ locate  => 用于查找文件, 它比find命令的搜索速度快
  
$ touch filename     => 创建一个空文件
  
$ rename             => 重命名一个或多个文件(使用有问题，用mv实现同样的功能)
  
$ mv source destination  => 移动目录或文件
    # 可以用来重命名文件或目录
  
$ cp source destination  => 复制
　　参数
　　-a 尽可能将档案状态、权限等资料都照原状予以复制.
	-R 和-r差不多
　　-r 若 source 中含有目录名，则将目录下之档案亦皆依序拷贝至目的地.
　　-f 若目的地已经有相同档名的档案存在，则在复制前先予以删除再行复制.

　　例:
　　将档案 aaa 复制(已存在)，并命名为 bbb :
　　 cp aaa bbb

　　将所有的C语言程序拷贝至 Finished 子目录中 :
　　 cp *.c Finished

　　 cp /root/source .  # 将/root下的文件source复制到当前目录
  
$ rm  => 删除档案及目录(慎用删除不好恢复)
    & rm [options] name... 
　　参数:
    -i 删除前逐一询问确认.
    -f 即使原档案属性设为唯读，亦直接删除，无需逐一确认.
    -r 将目录及以下之档案亦逐一删除.
　　例:
　　删除所有C语言程序档；删除前逐一询问确认:
　　  rm -i *.c
　　将 Finished 子目录及子目录中所有档案删除:
　　  rm -r Finished
	删除目录下的所有文件除file1和file2外
	rm -rf !(file1|file2)
  
$ tar        =>  压缩解压
    $ tar -zcvf filename.tar.gz dirname  # 压缩
	    -c 建立压缩档案的参数指令(create的意思)
		-x 解开一个参数档案
		-t 查看tarfile里的档案
		c/x/t只能存在一个
		-z 是否同时具有gzip属性,即用gzip压缩
		-j 用bzip2压缩
		-v 压缩的过程中显示档案
		-f 使用档案名 注意:f之后要立即接档案名，不能再加参数

    $ tar -zxvf filename.tar.gz # 解压
  
$ zip/unzip
    $ zip -r mydata.zip mydir  # 压缩mydir目录
	   -x "test/*" # 排除某个文件
    $ unzip mydata.zip -d mydatabak
  
$ tar -xf ***.tar.bz2  # 解压tar.bz2
创建tar.xz文件: 先 tar cvf xxx.tar xxx/ 创建xxx.tar文件先, 然后使用 xz -z xxx.tar 来将 xxx.tar压缩成为 xxx.tar.xz
解压tar.xz文件: 先 xz -d xxx.tar.xz 将 xxx.tar.xz解压成 xxx.tar 然后, 再用 tar xvf xxx.tar来解包
```

#### 系统管理
```
$ route
$ iptraf       =>  查看网络流量
$ ifconfig -a  =>  显示网络配置
$ ipaddress    =>  查看ip
$ sudo ethstatus -i eth0  =>  查看网络流量
  
$ netstat    => 查看端口使用情况
    $ netstat -apn            =>  查看端口的占用情况
    $ netstat -apn|grep xxx   =>  查看xxxx端口的占用情况
	$ netstat -ntlp|grep xxx  =>  查看端口占用 
  
$ pstree # 树状显示进程和子进程的树
  
$ lsof -i    =>  查看端口占用情况
$ lsof -i:xxxx    =>  查看xxxx端口的占用情况
  
$ ps aux => 查看进程
$ ps aux|grep nginx
$ ps aux|grep <进程号>   =>  找到进程号后可以用此命令查看详细信息
  
$ ps      => 显示进程信息
    ps ux     # 显示当前用户的进程
    ps uxwww  # 显示当前用户的进程的详细信息
    ps aux    # 显示当前用户的进程
    ps ef     # 显示系统所有进程信息
	ps -em    # 显示 pid cmd
  
$ pgrep firefox  # 专门用于进程查询的grep
$ kill -l  # 列出所有的信号
# 只有第9种信号(SIGKILL)才可以无条件终止进程，其他信号进程都有权利忽略.
# 下面是常用的信号：
# HUP    1    终端断线
# INT    2    中断（同 Ctrl + C）
# QUIT   3    退出（同 Ctrl + \）
# TERM   15   终止
# KILL   9    强制终止
# CONT   18   继续（与STOP相反， fg/bg命令）
# STOP   19   暂停（同 Ctrl + Z）
  
$ kill  => 杀进程
    kill -s INT 【PID】  # -s 9 制定了传递给进程的信号是９, 即强制, 尽快终止进程
    kill -9 【PID】
	kill -HUP 【PID】 # 重启
  
$ pkill   # pkill = pgrep + kill	
$ pkill -9 -f `celery worker`
$ pkill -９ firefox
# pkill或者pgrep只要给出进程名的一部分就可以终止进程。
# killall和pkill是相似的,不过如果给出的进程名不完整，killall会报错 
$ killall
    killall -s INT 【进程名】
	killall -9 【进程名】
  
$ ps -ef | grep firefox | grep -v grep | cut -c 9-15 | xargs kill -s 9	
$ pgrep firefox | xargs kill -s 9  # 上一行的改进
$ pgrep -f "celery worker"
说明:
“grep firefox”的输出结果是，所有含有关键字“firefox”的进程
“grep -v grep”是在列出的进程中去除含有关键字“grep”的进程
“cut -c 9-15”是截取输入行的第9个字符到第15个字符，而这正好是进程号PID
“xargs kill -s 9”中的xargs命令是用来把前面命令的输出结果（PID）作为“kill -s 9”命令的参数，并执行该命令。“kill -s 9”会强行杀掉指定进程。

$ tail  # 从指定点开始将文件写到标准输出
    -f  # 循环读取,f选项可以方便的查阅正在改变的日志文件
	    # tail -f filename会把filename里最尾部的内容显示在屏幕上,并且不断刷新,使你看到最新的文件内容
```

#### ssh
```bash
# 登录
ssh xue.bai@192.168.162.101 -p 3222  # enter ==> password
# 免密登陆
ssh-copy-id user@host -p 3222
# 传文件
# 从服务器上下载文件
scp username@servername:/path/filename /var/www/local_dir（本地目录）
# 上传本地文件到服务器
scp /path/filename username@servername:/path
# 传目录加 -r
```

#### nohup
```
# nohup就是不挂断的意思( no hang up)

command &    # 后台运行
普通进程用&符号放到后台运行, 如果启动该程序的控制台logout, 则该进程也会终止

nohup command [ Arg ... ] [ & ]
nohup <程序> &
则控制台logout后, 进程仍然继续运行, 起到守护进程的作用（虽然它不是严格意义上的守护进程）
使用nohup命令后, 如果不将 nohup 命令的输出重定向, 输出将附加到当前目录的 nohup.out 文件中, 起到了log的作用, 实现了完整的守护进程功能.

可以使用tail -f nohup.out监控输出

当shell中提示了nohup成功后还需要按终端上键盘任意键退回到shell输入命令窗口, 然后通过在shell中输入exit来退出终端; 
而我是每次在nohup执行成功后直接点关闭程序按钮关闭终端. 所以这时候会断掉该命令所对应的session, 导致nohup对应的进程被通知需要一起shutdown.

$ jobs        => 查看在后台运行的进程
$ ctrl + z    => 暂停进程转移到后台
$ bg          => 后台进程继续运行
$ fg %1       => 将后台进程移到前台
$ fg %n　     => 关闭

nohup启动的程序在进程执行完毕就退出, 而常见的一些服务进程通常永久的运行在后台, 不向屏幕输出结果.
在Unix中这些永久的后台进程称为守护进程（daemon）. 守护进程通常从系统启动时自动开始执行, 系统关闭时才停止


nohup command > myout.file 2>&1 &
说明: 0 – stdin (standard input), 1 – stdout (standard output), 2 – stderr (standard error);
2>&1是将标准错误（2）重定向到标准输出（&1）, 标准输出（&1）再被重定向输入到myout.file文件中.


# 在程序运行中清空nohup.out文件
cat /dev/null > nohup.out
cp /dev/null nohup.out
```

#### Linux中重定向命令行输出
```
Linux环境中支持输入输出重定向, 用符号<和>来表示.
0、1和2分别表示标准输入、标准输出和标准错误信息输出
特殊的文件描述符/dev/null, 它就像一个黑洞, 所有重定向到它的信息都会消失得无影无踪. 这一点非常有用,
当我们不需要回显程序的所有信息时, 就可以将输出重定向到/dev/null
$ ls 1>/dev/null 2>/dev/null  => 标准输出和标准错误都重定向到/dev/null
$ ls >/dev/null 2>&1          => 将错误重定向到标准输出, 然后再重定向到 /dev/null

$ ls -l > lee.dat    => 将执行"ls -l"命令的结果写入文件 lee.dat 中

$ 命令>! 文件   => 将命令的执行结果送至指定的文件中，若文件已经存在，则覆盖
$ ls -lg >! lee.dat  => 将执行"ls -lg"命令的结果覆盖写入文件 lee.dat 中

$ 命令>& 文件   => 将命令执行时屏幕上所产生的任何信息写入指定的文件中
$ cc lee.c >& lee.dat  => 将编译 lee.c 文件时所产生的任何信息写入文件 lee.dat 中

$ 命令>> 文件    => 将命令执行的结果附加到指定的文件中.
$ ls -lag >> lee.dat 将执行 "ls -lag" 命令的结果附加到文件 lee.dat 中

$ 命令>>& 文件   => 将命令执行时屏幕上所产生的任何信息附加到指定的文件中
cc lee.c >>& lee.dat 将编译 lee.c 文件时屏幕所产生的任何信息附加到文件 lee.dat 中


linux文件描述符:可以理解为linux跟踪打开文件, 而分配的一个数字,这个数字有点类似c语言操作文件时候的句柄,
通过句柄就可以实现文件的读写操作.
用户可以自定义文件描述符范围是:3-num,这个最大数字,跟用户的:ulimit –n 定义数字有关系,不能超过最大值

linux启动后, 会默认打开3个文件描述符, 分别是:
标准输入 standard input 0;
标准输出 standard output 1;
错误输出 error output 2;

以后打开文件后, 新增文件绑定描述符可以依次增加, 一条shell命令执行, 都会继承父进程的文件描述符, 因此, 所有运行的shell命令, 都会有默认3个文件描述符.
```

#### 输出重定向
```
$ command-line1 [1-n] > file或文件操作符或设备

$ command-line [n] < file或文件描述符&设备

$ cmd < file cmd 命令以 file 文件作为 stdin

$ cat <>file 以读写的方式打开 file

$ cmd < file > file2 cmd 命令以 file 文件作为 stdin，以 file2 文件作为 stdout

$ nohup ./program >/dev/null 2>log &    => 舍弃标准输出，将错误输出到log文件中

$ nohup ./program >/dev/null 2>&1 &     => 如果错误信息也不想要的话
```

#### 源码编译安装软件
```
一般3个步骤组成:
配置(configure);
编译(make);
安装(make install);
  
configure是一个可执行脚本, 它有很多选项, 在待安装的源码路径下使用命令./configure –help输出详细的选项列表.
其中--prefix选项是配置安装的路径,如果不配置该选项, 安装:
可执行文件默认放在/usr/local/bin;
库文件默认放在/usr/local/lib;
配置文件默认放在/usr/local/etc;
其它的资源文件放在/usr/local/share; 比较凌乱.
如果配置--prefix 如:
./configure --prefix=/usr/local/test
可以把所有资源文件放在/usr/local/test的路径中, 不会杂乱.
用了—prefix选项的另一个好处是卸载软件或移植软件, 当某个安装的软件不再需要时,只须简单的删除该安装目录,
就可以把软件卸载得干干净净;移植软件只需拷贝整个目录到另外一个机器即可（相同的操作系统）
当然要卸载程序, 也可以在原来的make目录下用一次make uninstall, 但前提是make文件指定过uninstall。
```

#### 开机启动
```
# 查看当前系统的运行级别
$ who -r 
$ runlevel
# Ubuntu的默认开机的runlevel是2
# 运行级别配置文件/etc/init/rc-sysinit.conf

# Ubuntu开机启动顺序
init --> rcS.d下的脚本 --> rcN.d下的脚本 --> rc.local
  
# sysv-rc-conf 管理开机启动
$ sudo apt-get install sysv-rc-conf
$ sudo sysv-rc-conf
  
# 直接修改/etc/rc0.d ~ /etc/rc6.d和/etc/rcS.d下的脚本
# S开头的表示启动，K开头的表示不启动, S/K后边的数字表示优先级[0-99].
$ sudo mv /etc/rc2.d/S20mysql /etc/rc2.d/K20mysql
  
# update-rc.d 管理开机启动
# update-rc.d <service name> start|stop| <order number> <run levels>
$ sudo update-rc.d rinetd start 20 2
$ sudo update-rc.d rinetd stop 20 0
  
# update-rc.d <service name> enable|disable  <runlevels>
$ sudo update-rc.d rinetd disable 2 在runlevel2中暂时禁止该服务
  
# update-rc.d <service name> default [NN | SS KK]
$ sudo update-rc.d rinetd default 80 80
# default 表示在2 3 4 5 中添加80(the first 80)顺序的Start，在0 6 中添加80(the second 80)顺序的Kill服务
  
# 删除启动项(移除了rc[1-6].d目录里的启动脚本链接)
sudo update-rc.d -f apache2 remove
sudo update-rc.d -f nginx remove
  
# 禁止mysql开机启动
$ sudo update-rc.d mysql disable [runlevel]
  
# debian的runlevel
0 – Halt，关机模式
1 – Single，单用户模式
2 - Full multi-user with display manager (GUI)
3 - Full multi-user with display manager (GUI)
4 - Full multi-user with display manager (GUI)
5 - Full multi-user with display manager (GUI)
6 - Reboot，重启
  
# redhat的runlevel
0 - 关机. 不能将系统缺省运行级别设置为0，否则无法启动.
1 - 单用户模式，只允许root用户对系统进行维护.
2 - 多用户模式，但不能使用NFS（相当于Windows下的网上邻居）
3 - 字符界面的多用户模式.
4 - 未定义.
5 - 图形界面的多用户模式.
6 - 重启. 不能将系统缺省运行级别设置为0，否则会一直重启.
  
# S 全都有
  
# 可以在不重新启动操作系统的前提下，切换操作系统的RunLevel
$ sudo init <num>
```
