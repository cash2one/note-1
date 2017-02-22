# 开启管理web服务
sudo rabbitmq-plugins enable rabbitmq_management
# 管理页面的地址
http://host:55672/

# 配置文件
/etc/rabbitmq/rabbitmq.conf
[
    {rabbit, [{disk_free_limit, {mem_relative, 0.1}}]}
].
# 注意结尾处有个"."

/et/rabbitmq/rabbitmq-env.conf
# rabbitmq环境变量的配置
RABBITMQ_CONFIG_FILE = /etc/rabbitmq/rabbitmq.conf
RABBITMQ_MNESIA_BASE 指定MNESIA数据库存储的位置

# 问题记录
磁盘空间不足, 发送消息时会一直阻塞, 直到磁盘有空间.

