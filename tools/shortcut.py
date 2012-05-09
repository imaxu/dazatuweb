# -*- coding: utf-8 -*-
'''内部调用的快捷方法
	CREATED DATE:2011-12-31
	CREATED BY: xuwh
'''
import datetime
def get_time_now(format_str='%Y-%m-%d %H:%M:%S'):
	'''获取当前时间，并以指定格式输出
		args:
			format_str - 指定的时间格式
						%y 两位数的年份表示（00-99）
						%Y 四位数的年份表示（000-9999）
						%m 月份（01-12）
						%d 月内中的一天（0-31）
						%H 24小时制小时数（0-23）
						%I 12小时制小时数（01-12） 
						%M 分钟数（00=59）
						%S 秒（00-59）

						%a 本地简化星期名称
						%A 本地完整星期名称
						%b 本地简化的月份名称
						%B 本地完整的月份名称
						%c 本地相应的日期表示和时间表示
						%j 年内的一天（001-366）
						%p 本地A.M.或P.M.的等价符
						%U 一年中的星期数（00-53）星期天为星期的开始
						%w 星期（0-6），星期天为星期的开始
						%W 一年中的星期数（00-53）星期一为星期的开始
						%x 本地相应的日期表示
						%X 本地相应的时间表示
						%Z 当前时区的名称
						%% %号本身 		
		return:
			string - 指定格式的时间字符串
	'''
	import time
	return time.strftime(format_str,time.localtime(time.time()))

def get_timedelta_between_times(time1=datetime.datetime.now(),time2=datetime.datetime.now()):
	'''获取指定时间之间的差
		args:
			time1 - 时间变量1，datetime类型，默认是服务器现在时间
			time2 - 时间变量2，datetime类型，默认是服务器现在时间
		return:
			datetime.timedelta - datetime.timedelta类型
	'''
	return (time2-time1)
	
def get_timedelta_between_timestr(time_str1='1900-01-01 00:00:00',time_str2=get_time_now(),format='%Y-%m-%d %H:%M:%S'):
	'''获取指定时间字符串之间的差
		args:
			time_str1 - 时间变量1，string类型 默认为 1900-01-01 00:00:00
			time_str2 - 时间变量2，string类型 默认为当前服务器本地时间
			format	  - 时间格式字符串，默认为 %Y-%m-%d %H:%M:%S
		return:
			datetime.timedelta - datetime.timedelta类型
	'''
	__time1 = datetime.datetime.strptime(time_str1,format)
	__time2 = datetime.datetime.strptime(time_str2,format)
	return get_timedelta_between_times(__time1,__time2)
	
def get_seconds_from_timedelta(timedelta=datetime.timedelta(0)):
	'''获取传入的timedelta对象等价的秒数
		args:
			timedelta - datetime.timedelta对象，默认值为0
		return:
			int - 与timedelta等价的秒数
	'''
	__ret = 0
	if timedelta.days > 0:
		__ret = timedelta.days * 24 * 3600
	return __ret + timedelta.seconds
	
def wrapped_render_to_response(temppath,tags):
	'''重新封装的render_to_response
	'''
	from django.shortcuts import render_to_response
	return render_to_response(
		temppath,
		tags
	)
