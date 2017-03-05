MySQL Note
==========
####　导语:
> 与其他的大型数据库例如 Oracle, DB2, SQL Server等相比, MySQL自有它的不足之处,
但是这丝毫也没有减少它受欢迎的程度. 对于一般的个人使用者和中小型企业来说, MySQL提供的功能已经绰绰有余,
而且由于MySQL是开放源码软件, 因此可以大大降低总体拥有成本.

## 数据库管理

#### 1. 启动MySQL
```
$ /etc/init.d/mysql start(stop, restart)
$ service mysql start(stop, restart)
$ systemctl stop(start, restart) mysql.service
```
#### 2. 登录MySQL
```
$ mysql -h hostname -u username -p passwd -P port;
```
#### 3. 查看数据库基本信息
```
$ mysql> \s;
$ mysql> status;
```
#### 4. 查看help
```
$ mysql> \h;
$ mysql> help;
$ mysql> help cmd;
```
#### 4. 创建用户
```
$ mysql> CREATE USER 'username'@'host' IDENTIFIED BY 'passwd';
```
> * username -> 创建的用户名
> * host -> 指定该用户在哪个主机上可以登陆(localhost:本地; %:任意主机)
> * passwd -> 密码, 为空代表无密码

例:

    $ mysql> CREATE USER 'pig'@'localhost' IDENTIFIED BY '123456';
    $ mysql> CREATE USER 'pig'@'192.168.1.101' IDENDIFIED BY '123456';
    $ mysql> CREATE USER 'pig'@'%' IDENTIFIED BY '123456';
    $ mysql> CREATE USER 'pig'@'localhost';

#### 4. 删除用户
```
$ mysql> DROP USER 'username'@'host';
```
#### 5. 授权
```
$ mysql> GRANT privileges ON db.table TO 'username'@'host';
```
> * privileges -> 用户操作权限, 如: SELECT, INSERT, UPDATE等, 所有权限可以使用ALL;
> * db -> 数据库名;
> * table -> 表名;
> * 如果要授予该用户对所有数据库和表的相应操作权限则可用\*表示, 如\*.\*.

例:

    $ mysql> GRANT select, insert ON school.* TO 'lin'@'%';
    $ mysql> GRANT ALL ON *.* TO 'pig'@'%';

> 注意: 用以上命令授权的用户不能给其它用户授权, 如果想让该用户可以授权, 用以下命令:

    $ mysql> GRANT privileges ON db.table TO 'username'@'host' WITH GRANT OPTION;

#### 6. 设置与更改用户密码
```
$ mysql> SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');
$ mysql> SET PASSWORD = PASSWORD("newpassword");  (如果是当前登陆用户用)
$ mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'xxxx';  (修改别人的密码)
```
#### 7. 撤销用户权限
```
* $ mysql> REVOKE privileges ON db.table FROM 'username'@'host';
```
例:

    $ mysql> REVOKE select ON *.* FROM 'pig'@'%';

> 注意:
假如你在给用户'pig'@'%'授权的时候是这样的(或类似的):
GRANT SELECT ON test.user TO 'pig'@'%',
则在使用REVOKE SELECT ON *.* FROM 'pig'@'%';
命令并不能撤销该用户对test数据库中user表的SELECT 操作.
相反,如果授权使用的是GRANT SELECT ON *.* TO 'pig'@'%';
则REVOKE SELECT ON test.user FROM 'pig'@'%';
命令也不能撤销该用户对test数据库中user表的Select 权限.

#### 8. 查看权限
```
$ mysql> SHOW GRANTS FOR 'pig'@'%';
```
#### 9. 查看所有的数据库名字
```
$ mysql> SHOW DATABASES;
```
#### 10. 设置创建的数据库的编码
```
$ mysql> ALTER DATABASE 数据库名 CHARACTER SET utf8;
```
#### 11. 查看数据库编码
```
$ mysql> SHOW CREATE DATABASE 数据库名;
$ mysql> SHOW variables LIKE 'character%';
```
#### 12. 选择一个数据库操作
```
$ mysql> USE 数据库名;
$ mysql> SELECT database();  # 查看当前数据库
```
#### 13. 查看当前数据库下所有的表名
```
$ mysql> SHOW TABLES;
```
#### 14. 创建一个数据库
```
$ mysql> CREATE DATABASE 数据库名;
$ mysql> CREATE DATABASE 数据库名 DEFAULT CHARACTER SET utf8;
```
#### 15.删除一个数据库
```
$ mysql> DROP DATABASE 数据库名;
$ mysql> DROP DATABASE IF EXISTS 数据库名
```
#### 16. 查看表结构
```
$ mysql> SHOW COLUMNS FROM 表名;
$ mysql> DESC 表名;
$ mysql> SHOW CREATE TABLE 表名;
```

----
#### 8.创建一个表
* $ mysql> CREATE TABLE 表名( uid BIGINT(20) NOT NULL, uname VARCHAR(20) NOT NULL);

例:
```sql
CREATE TABLE
    USER
    (
        name VARCHAR(30) NOT NULL,
        id INT DEFAULT '0' NOT NULL,
        stu_id INT,
        phone VARCHAR(20),
        address VARCHAR(30) NOT NULL,
        age INT(4) NOT NULL,
        PRIMARY KEY (name),
        CONSTRAINT stu_id UNIQUE (stu_id)
    )
    ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

#### 9. 删除一个表
```
$ mysql> DROP TABLE 表名;
$ mysql> ALTER TABLE 表名 DROP COLUMN column-name
```
* $ 清空表数据
```
mysql> DELETE FROM 表名;
mysql> TRUNCATE TABLE 表名;  --不记录mysql日志, 无法恢复数据
```
* $ 删除表中的某些数据
```
mysql> DELETE FROM 表名 WHERE 表达式;
mysql> DELETE FROM 表名 WHERE id=1;
```
#### 14.查看表里的数据
```
mysql> SELECT * FROM 表名 LIMIT 10 OFFSET (SELECT COUNT(*) FROM 表明);  # 倒数10条
mysql> SELECT * FROM 表名 LIMIT (SELECT COUNT(*) FROM 表明), 10;  # 倒数10条
mysql> SELECT * FROM 表名 ORDER BY id DESC LIMIT 10;  # 倒数10条

```
#### 15. 修改表的列与表名
* 给列更名
```
$ mysql> ALTER TABLE 表名 CHANGE 旧字段名 新字段名;
```
* 给表更名
```
$ mysql> ALTER TABLE 旧表名 RENAME 新表名;
```
* 修改某个表的字段类型及指定为空或非空
```
$ mysql> ALTER TABLE 表名 CHANGE 字段名 字段类型 [是否允许非空];
$ mysql> ALTER TABLE 表名 MODIFY 字段名 字段类型 [是否允许非空];
```
* 修改某个表的字段名称及指定为空或非空
```
$ mysql> ALTER TABLE 表名 CHANGE 字段原名称 字段新名称 字段类型 [是否允许非空];
```
* 例: 修改表expert_info中的字段birth,允许其为空
```
$ mysql> ALTER TABLE expert_info CHANGE birth birth varchar(20) null;
```
#### 16. 修改表中的数据
* 增加一个字段(一列)
```
$ mysql> ALTER TABLE 表名 ADD COLUMN column_name type default value; 字段mi字段名字段字段
```
> (type指该字段的类型,value指该字段的默认值)

* 更改一个字段名字(也可以改变类型和默认值)
```sql
ALTER TABLE table_name CHANGE sorce_col_name dest_col_name type default value;
```
> (source_col_name指原来的字段名称,dest_col_name)

例:
```sql
ALTER TABLE Board_Info CHANGE IsMobile IsTelphone int(3) unsigned default1;
-- 改变一个字段的默认值
ALTER TABLE table_name ALTER column_name SET DEFAULT value;
```
例:
```sql
ALTER TABLE book ALTER flag SET DEFAULT '0′;
-- 改变一个字段的数据类型
ALTER TABLE table_name CHANGE COLUMN column_name column_name type;
```
例:
```sql
ALTER TABLE userinfo CHANGE COLUMN username username VARCHAR(20);
-- 向一个表中增加一个列做为主键
ALTER TABLE table_name add COLUMN column_name type AUTO_INCREMENT PRIMARYKEY;
```
例:
```sql
ALTER TABLE book ADD COLUMN id INT(10) AUTO_INCREMENT PRIMARY KEY;
```
#### 12.表复制及备份还原
* 复制表结构
```sql
$ mysql> CREATE TABLE 新表名 LIKE book;  -- 含有主键等信息的完整表结构
```
* 只有表结构,没有主键等信息
```sql
$ mysql> CREATE TABLE 新表名 SELECT * FROM books;
$ mysql> CREATE TABLE 新表名 as(select * from book);
$ mysql> CREATE TABLE 新表名 SELECT * FROM books WHERE 1=2;
```
* 将旧表中的数据灌入新表(新表必须已经存在)
```sql
$ mysql> INSERT INTO 新表 SELECT * FROM 旧表;
```
#### 13.备份与还原
* 只导出表结构不导数据
```
$ mysqldump --opt -d 数据库名 -u root -p > xxx.sql
```
* 导出数据和结构
```
$ mysqldump -h hostname -u username -p database-name > backupfile.sql
$ mysqldump -h hostname -u username -p database-name | gzip > backupfile.sql.gz
```
* 还原MySQL数据库的命令
```
$ mysql> source test.sql;
$ mysql -h hostname -u username -p database-name < backupfile.sql
$ gunzip < backupfile.sql.gz | mysql -u username -p password databasename
```
#### 17. 数据库某表的备份, 在命令行中输入
```
$ mysqldump -u root -p database_name table_name > bak_file_name
```
例:

    $ mysqldump -hhostname -uroot -ppasswd 库名 表名 > user_info.dat

#### 18. 导出数据
```
select_statment into outfile"dest_file";
```
例:

    select cooperatecode, screatetime from publish limit 10 intooutfile”/home/mzc/temp/tempbad.txt”;

#### 19. 导入数据
```
load data infile "file_name" into table table_name;
```
例:

    load data infile"/home/mzc/temp/tempbad.txt" into table pad;

#### 20. 将两个表里的数据拼接后插入到另一个表里.

例: 下面的例子说明将t1表中的com2和t2表中的com1字段的值拼接后插入到tx表对应的字段里.

    $ mysql> INSERT INTO tx SELECT t1.com1, concat(t1.com2,t2.com1) FROM t1,t2;

#### 21. 删除字段
```
$ mysql> ALTER TABLE 表名 DROP COLUMN 列名;
```

#### 22. 字段唯一
```sql
-- 设置字段唯一
ALTER TABLE 表名 ADD unique('字段名')

-- 移除字段唯一
ALTER TABLE 表名 DROP INDEX field-name
```

## 查询表

> mysql查询的五种子句:
> * where(条件查询)
> * having（筛选）
> * group by（分组）
> * order by（排序）
> * limit（限制结果数）

#### 1. 查询数值型数据:
```sql
SELECT * FROM tb_name WHERE sum > 100;
```
> 查询谓词: >, =, <, <>, !=, !>, !<, =>, =<

#### 2. 查询字符串
```sql
SELECT * FROM student WHERE name='小刘';
SELECT * FROM student WHERE name like '刘%';
SELECT * FROM student WHERE name like '%程序员';
SELECT * FROM student WHERE name like '%PHP%';
```

#### 3. 查询日期型数据
```sql
SELECT * FROM tb_name WHERE date='2011-04-08';
```
> 注: 不同数据库对日期型数据存在差异
```
MySQL: SELECT * from tb_name WHERE birthday = '2011-04-08'
SQL Server: SELECT * from tb_name WHERE birthday = '2011-04-08'
Access: SELECT * from tb_name WHERE birthday = #2011-04-08#
```

#### 4. 查询逻辑型数据
```sql
SELECT * FROM tb_name WHERE type='T';
SELECT * FROM tb_name WHERE type='F';
```
> 逻辑运算符: AND OR NOT

#### 5. 查询非空数据
```sql
SELECT * FROM tb_name WHERE address <>'' ORDER BY addtime DESC;
```
> 注: <>相当于PHP中的!=

#### 6. 利用变量查询数值型数据
```sql
SELECT * FROM tb_name WHERE id = '$_POST[text]';
```
> 注: 利用变量查询数据时,传入SQL的变量不必用引号括起来,因为PHP中的字符串与数值型数据进行连接时,程序会自动将数值型数据转变成字符串,然后与要连接的字符串进行连接

#### 7. 利用变量查询字符串数据
```sql
SELECT * FROM tb_name WHERE name LIKE '%$_POST[name]%';
```
> 完全匹配的方法"%%"表示可以出现在任何位置

#### 8. 查询前n条记录
```sql
SELECT * FROM tb_name LIMIT 0, $N;
```

> limit语句与其他语句，如order by等语句联合使用，会使用SQL语句千变万化，使程序非常灵活

#### 9. 查询后n条记录
```sql
SELECT * FROM tb_name ORDER BY id ASC LIMIT $n;
```

#### 10. 查询从指定位置开始的n条记录
```sql
SELECT * FROM tb_name ORDER BY id ASC LIMIT [begin], $n;
```
> 注: 数据的id是从0开始的

#### 11. 查询统计结果中的前n条记录
```sql
SELECT * , (yw+sx+wy) AS total FROM tb_score ORDER BY (yw+sx+wy) DESC LIMIT 0, $num;
```

#### 12. 查询指定时间段的数据
```sql
SELECT 字段 FROM 表名 WHERE 字段名 BETWEEN 初始值 AND 终止值;
SELECT * FROM student WHERE age BETWEEN 0 AND 18;
```

#### 13. 按月查询统计数据
```sql
SELECT * FROM student WHERE month(date) = '[date]' ORDER BY date;
```
> 注: SQL语言中提供了如下函数, 利用这些函数可以很方便地实现按年、月、日进行查询
```
year(data): 返回data表达式中的公元年分所对应的数值
month(data): 返回data表达式中的月分所对应的数值
day(data): 返回data表达式中的日期所对应的数值
```

#### 14. 查询大于指定条件的记录
```sql
SELECT * FROM student WHERE age > [age] ORDER BY age;
```

#### 15. 查询结果不显示重复记录
```sql
SELECT DISTINCT 字段名 FROM 表名 WHERE 查询条件
```
> 注: SQL语句中的DISTINCT必须与WHERE子句联合使用，否则输出的信息不会有变化 ,且字段不能用*代替

#### 16. NOT与谓词进行组合条件的查询

* NOT BERWEEN … AND … 对介于起始值和终止值间的数据时行查询 可改成 <起始值 AND >终止值
* IS NOT NULL 对非空值进行查询
* IS NULL 对空值进行查询
* NOT IN 该式根据使用的关键字是包含在列表内还是排除在列表外，指定表达式的搜索，搜索表达式可以是常量或列名，而列名可以是一组常量，但更多情况下是子查询

#### 17. 显示数据表中重复的记录和记录条数
```sql
SELECT name, age, count(*), age FROM student WHERE age='19' group by date
```
#### 18. 对数据进行降序/升序查询
```sql
SELECT 字段名 FROM student WHERE 条件 ORDER BY 字段 DESC 降序
SELECT 字段名 FROM student WHERE 条件 ORDER BY 字段 ASC 升序
```
> 注: 对字段进行排序时若不指定排序方式，则默认为ASC升序

#### 19. 对数据进行多条件查询
```sql
SELECT 字段名 FROM student WHERE 条件 ORDER BY 字段1 ASC 字段2 DESC …
```
> 注: 对查询信息进行多条件排序是为了共同限制记录的输出，一般情况下，由于不是单一条件限制，所以在输出效果上有一些差别。

#### 20. 对统计结果进行排序
* 函数SUM([ALL]字段名) 或 SUM([DISTINCT]字段名),可实现对字段的求和,函数中为ALL时为所有该字段所有记录求和,若为DISTINCT则为该字段所有不重复记录的字段求和
```sql
SELECT name, SUM(price) AS sumprice FROM tb_price GROUP BY name
SELECT * FROM tb_name ORDER BY mount DESC, price ASC
```
#### 21. 单列数据分组统计
```sql
SELECT id, name, SUM(price) AS title, date FROM tb_price GROUP BY pid ORDER BY title DESC
```
> 注: 当分组语句group by排序语句order by同时出现在SQL语句中时，要将分组语句书写在排序语句的前面，否则会出现错误

#### 22. 多列数据分组统计
* 多列数据分组统计与单列数据分组统计类似
```sql
SELECT *, SUM(字段1*字段2) AS (新字段1) FROM 表名 GROUP BY 字段 ORDER BY 新字段1 DESC
SELECT id, name, SUM(price*num) AS sumprice FROM tb_price GROUP BY pid ORDER BY sumprice DESC
```
> 注: group by语句后面一般为不是聚合函数的数列，即不是要分组的列

#### 23. 多表分组统计
```sql
SELECT a.name, AVG(a.price), b.name, AVG(b.price) FROM tb_demo058 AS a, tb_demo058_1 AS b WHERE a.id=b.id GROUP BY b.type;
```
