MongoDB
=====
## 安装
```
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10

$ echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb.list

$ sudo apt-get update
$ sudo apt-get install mongodb-org

$ apt-get install mongodb-org=3.0.0 mongodb-org-server=3.0.0 mongodb-org-shell=3.0.0 mongodb-org-mongos=3.0.0 mongodb-org-tools=3.0.0


$ sudo service mongod start
$ sudo service mongod stop
$ mongo --version
```

#### 开启mongodb
```
$ mongod
```
#### 打开client
```
$ mongo
```
