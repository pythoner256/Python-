"""time模块"""

#  time模块中时间表现的格式主要有三种：
#
# 　　a、timestamp时间戳，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量
#
# 　　b、struct_time时间元组，共有九个元素组。
#
# 　　c、format time 格式化时间，已格式化的结构使时间更具可读性。包括自定义格式和固定格式。


import time


time.time()  # 1532525965.4503942 生成时间戳

time.ctime()  # 'Wed Jul 25 21:45:48 2018' 输出字符串格式

time.sleep(1)  # 睡眠1秒，参数单位为妙

time.localtime()  # 将一个时间戳转换为当前时区的struct_time；time.struct_time(
#                                                                       tm_year=2018,
#                                                                       tm_mon=7,
#                                                                       tm_mday=25,
#                                                                       tm_hour=21,
#                                                                       tm_min=45,
#                                                                       tm_sec=22,
#                                                                       tm_wday=2,
#                                                                       tm_yday=206,
#                                                                       tm_isdst=0
#                                                                       )

time.strftime("%a %b %d %H:%M:%S %Y")  # 'Wed Jul 25 21:51:23 2018' 格式化时间和日期，参数给定的是默认格式

"""datetime模块"""

import datetime

# datetime模块用于是date和time模块的合集

# datetime模块定义了5个类，分别是
#
# 1.datetime.date：表示日期的类
#
# 2.datetime.datetime：表示日期时间的类
#
# 3.datetime.time：表示时间的类
#
# 4.datetime.timedelta：表示时间间隔，即两个时间点的间隔
#
# 5.datetime.tzinfo：时区的相关信息

datetime.datetime(2018, 7, 25, 22, 13, 49)  # 2018-07-25 22:09:59 返回时间日期格式

datetime.datetime.today()  # 2018-07-25 22:09:59.343287 返回当前日期和时间

datetime.datetime.now()  # 返回的结果跟today一样的

datetime.datetime.strftime()  # 自定义格式化时间


