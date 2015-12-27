Supervisor --  Python写的进程管理器.不仅仅可以用来管理进程,还可以用来做开机启动.

   用途就是有一个进程需要每时每刻不断的跑,但是这个进程又有可能由于各种原因有可能中断.
   当进程中断的时候我希望能自动重新启动它,此时,我就需要使用到了Supervisor

这个工具主要就两个命令:
supervisord : supervisor的服务器端部分，启动supervisor就是运行这个命令;
supervisorctl：启动supervisor的命令行窗口;

生成配置文件(supervisord.conf)
echo_supervisord_conf > /etc/supervisord.conf

在supervisord.conf最后增加(分号后边的表示注释，可以不写)


ctl中： help //查看命令;
ctl中： status //查看状态;

注意:如果修改了 /etc/supervisord.conf, 需要执行 supervisorctl reload 来重新加载配置文件, 否则不会生效

