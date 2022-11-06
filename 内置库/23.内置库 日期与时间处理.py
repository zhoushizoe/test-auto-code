"""
获取当前日期/获取特定时间
datetime与datestamp时间戳互换
datetime与str互换
实战练习
工作中应用：
    作为日志信息的内容输出
    计算某个功能的执行时间
    用日期命令一个日志文件的名称
    生成随机数（时间是不会重复的）
"""
"""
python中处理时间的模块
    time
    datetime
    calendar
常见的时间表现形式
    时间戳 1970年1月1日为零点
    格式化的时间字符串
"""
"""
datetime常用的类
    datetime（from datetime import datetime）时间日期相关
    timedelta（from datetime import timedelta）计算两个时间的时间差
    timezone（from datetime import timezone）时区相关
"""
import datetime
# 获取当前时间 .now
now = datetime.datetime.now()
print(now)
# 获取指定时间,输入指定时间
assign = datetime.datetime(2022, 10, 31)
print(assign.timestamp())
# 当前处于第几天，几号
print(now.day)
# 当前处于第几个月
print(now.month)
# 当前处于的年份
print(now.year)
# 当前时间转成时间戳
print(now.timestamp())
"""
字符串与时间的互转
"""
# 将字符串转换为datetime
s = "2022-10-30 15:03:58"
s1 = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")  # 使用strptime转换
print(s1)
# 将时间转换为字符串
now_time = datetime.datetime.now()
print(now_time)
# %a为一周中的第几天；%b为月份；%d：一月中的第几天；
change = now_time.strftime("%a %b %d %H:%M")
print(change)

# practice_1 = datetime.datetime.now()
# # 将时间转换成字符串
# now_3 = practice_1.strftime("%a %b %d %H:%M")  # strftime 将时间转换成字符串
# print(now_3)
# 将字符串转换成时间
# time_str = "2022-10-30 15:03:58"
# time_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
# print(time_time)
# print(type(time_time))
"""
时间戳与时间之间的转换
"""
# # 获取时间戳：
# stamp = now.timestamp()
# print(stamp)
# # 将时间戳转换为时间 fromtimestamp
# change_time = datetime.datetime.fromtimestamp(stamp)
# print(change_time)
# 将时间转换成时间戳
date_stamp = datetime.datetime.now()
print(date_stamp.timestamp())
# 将时间戳转换成时间
# s_1 = 1667116025.555471
# print(datetime.datetime.fromtimestamp(s_1))
s_2 = 1667116168.902798
print(datetime.datetime.fromtimestamp(s_2))
# 时间转化成时间戳
s_3 = datetime.datetime(2022, 2, 2)
print(s_3.timestamp())
"""
写一段代码，生成一个以时间命名的日志文件。并向日志文件中写入日志数据
"""
# 获取当前时间
# now_time_2 = datetime.datetime.now()
# c_time = now_time_2.strftime("%Y%m%d_%H%M%S")
# print(c_time)
# log_name = c_time + ".log"
# with open(log_name, "w", encoding="utf-8") as f:
#     print(f.write("这是一个以时间为命名的log文件"))
"""
总结：
    获取当前时间：datetime.datetime.now()
    当前时间转成时间戳: now = datetime.datetime.now();now.timestamp()
    时间戳转换成时间：
                s_1 = 1667116025.555471
                print(datetime.datetime.fromtimestamp(s_1))
    将字符串转换为时间：s = "2022-10-30 15:03:58"
                    s1 = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    将时间转换为字符串：practice_1 = datetime.datetime.now()
                     now_3 = practice_1.strftime("%a %b %d %H:%M") 
                     print(now_3)
"""


