# -*- coding: utf-8 -*-
'''
	MODEL NAME:		tools.log
	CREATED BY:		xuwh
	CREATED DATE:	2011-12-19
'''
from settings import LOG_ROOT
import time
def writelog(text):
	log_txt = 'system log is written by: %s' % (text,)
	_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	_time = time.strftime('%H:%M:%S',time.localtime(time.time()))
	log_file_path = LOG_ROOT + 'log_%s.txt' % (_date,)
	fil = open(log_file_path,'a')
	try:
		fil.write(
			('[%s]' % (_time,)) + log_txt + '\n')
	except:
		pass
	finally:
		fil.close()