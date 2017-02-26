dpkg的使用
=========

dpkg -i <.deb file name>  安装

dpkg -r package  删除软件包（保留其配置信息）

dpkg -P  删除一个包（包括配置信息）

dpkg -L package  显示一个包安装到系统里面的文件目录信息,用此命令查看软件安装到什么地方

dpkg –version  显示dpkg的版本号

dpkg -c filename  显示一个Deb文件的目录

dpkg -I filename [control-file]  显示一个Deb的说明

dpkg -s package  查找包的详细信息

dpkg -I vim  搜索Deb包

dpkg –configure package     配置包


1、搜狗拼音输入法
官网下载.deb包
$ sudo dpkg -i xxx.deb

2、bumblebee
处理双显卡发热问题
ubuntu官方论坛方法

3、vim
$ sudo apt-get install vim

安装youcompleteme
sudo apt-get install vim
sudo apt-get install vim-youcompleteme
sudo apt-get install vim-addon-manager
vam install youcompleteme

4、git和svn
$ sudo apt-get install git
$ sudo apt-get install subversion

5、chrome
下载.deb包
$ sudo dpkg -i chrome-xxx.deb
安装会出错,下面命令解决
$ sudo apt-get -f install

6、mysql
$ sudo apt-get update
$ sudo apt-get install mysql-server mysql-client

7、Oracle JDK
$ sudo add-apt-repository ppa:webupd8team/java
$ sudo apt-get update
$ sudo apt-get install oracle-java8-installer
$ sudo apt-get install oracle-java8-set-default

8、pycharm


9、sublime text3
sudo apt-get install libgtk2.0-dev


10、openvpn
$ sudo apt-get install openvpn


11、mongodb


12、redis


13、nginx
$ sudo add-apt-repository ppa:nginx/stable
$ sudo apt-get update
$ sudo apt-get install nginx

$ sudo cd /usr/local/nginx
$ sudo sbin/nginx

访问localhost:8080


14、右键打开终端
$ sudo apt-get install nautilus-open-terminal


15、依赖库
python-dev
libssl-dev
libffi-dev

lxml
错误：libxml/xmlversion.h：没有那个文件或目录
apt-get install libxml2-dev
sudo ln -s /usr/include/libxml2/libxml   /usr/include/libxml
错误：libxslt/xsltconfig.h：没有那个文件或目录
apt-get install libxslt-dev

pycurl
错误：Could not run curl-config
sudo apt-get install libcurl4-openssl-dev

pillow
$ sudo apt-get install libjpeg-dev

16、config

sudo apt-get build-dep python

# install python
./configure
sudo make
(
tk-dev; libgdbm-dev; libdb5.1-dev 
)
sudo make install

# mysql_config not found
libmysqld-dev
libmysqlclient-dev

# pip
sudo apt-get install openssl
sudo apt-get install libssl-dev

# sqlite3
sudo apt-get install libsqlite3-dev

#lxml
sudo apt-get install libxml2-dev libxslt-dev python-dev

# 线缆被拔出的问题
##关闭了网卡的自动协商功能，设置网卡在100M下工作，设置全双工的工作模式
sudo ethtool -s eth0 autoneg off speed 100 duplex full

在/etc/init.d/rc.local里添加
/sbin/ethtool -s eth0 autoneg off speed 100 duplex full

auto eth0
iface eth0 inet dhcp

sudo service network-manager stop
sudo rm /var/lib/Network-Manager/Network-Manager.state
sudo service network-manager start

# 多版本gcc切换
## 配置
$ sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.4 40
$ sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.4 40
$ sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-3.4 30
$ sudo update-alternatives --install /usr/bin/gcc g++ /usr/bin/g++-3.4 30
## 切换
$ sudo update-alternatives --config gcc
$ sudo update-alternatives --config g++

