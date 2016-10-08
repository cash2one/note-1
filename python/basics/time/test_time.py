# -*- coding: utf-8 -*-
import time
import datetime
import calendar


"""
时间的表示方式
1. 时间戳 -- 时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量, 时间戳是惟一的.
2. 元组(struct_time) -- struct_time元组共有9个元素
    year (four digits, e.g. 1998)
    month (1-12)
    day (1-31)
    hours (0-23)
    minutes (0-59)
    seconds (0-59)
    weekday (0-6, Monday is 0)
    Julian day (day in the year, 1-366)
    DST (Daylight Savings Time) flag (-1, 0 or 1) 是否是夏令时
    If the DST flag is 0, the time is given in the regular time zone;
    if it is 1, the time is given in the DST time zone;
    if it is -1, mktime() should guess based on the date and time.
3. 格式化字符串
"""

# ****************************************************************************
# time
# ****************************************************************************

print time.sleep(0.001)  # 线程推迟指定的时间运行, 单位为秒.

print time.time()  # 返回当前时间的时间戳
print time.clock()  # 返回的是程序运行时间
print time.ctime()  # 把一个时间戳转化为time.asctime()的形式

print time.localtime()  # 将一个时间戳转换为当前时区的struct_time, 参数未提供则以当前时间为准.
print time.gmtime()  # gmtime()方法是将一个时间戳转换为UTC时区(0时区)的struct_time.

print time.mktime(time.localtime())  # 将一个struct_time转化为时间戳

print time.asctime()  # 把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'


print time.strftime('%Y-%m-%d %H:%M:%S')
print time.strptime('2015-12-1 12:10:32', '%Y-%m-%d %H:%M:%S')  # 将时间字符串根据指定的格式化符转换成struct_time

time.tzset()  # 重设时区


# ****************************************************************************
# datetime模块定义了下面这几个类:
# datetime.date: 表示日期的类, 常用的属性有year, month, day.
# datetime.time: 表示时间的类, 常用的属性有hour, minute, second, microsecond.
# datetime.datetime: 表示日期时间.
# datetime.timedelta: 表示时间间隔, 即两个时间点之间的长度.
# datetime.tzinfo：与时区有关的相关信息.
# 注: 上面这些类型的对象都是不可变(immutable)的
# ****************************************************************************
print datetime.date(2012, 9, 3)
print datetime.time(hour=12, minute=12, second=12, microsecond=12, tzinfo=None)
print datetime.datetime(2012, 9, 3, hour=12, minute=13, second=31, microsecond=345, tzinfo=None)
print datetime.timedelta()
print datetime.tzinfo()


# ****************************************************************************
# calender
# calendar 模块是 Unix cal 命令的Python实现, 它可以将给定年份/月份的日历输出到标准输出设备上.
# ****************************************************************************
print calendar.prmonth(2016, 12)
print calendar.prcal(2015)
