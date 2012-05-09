# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response

from task.models import Task
import settings
def index(request):
	#初始化一段打杂兔的临时数据
	dazatu_list = [
		{'id':1,
		'name':'李小梅',
		'level':10,
		'goodat':['编织','儿童看护','室内保洁'],
		'image':'id_20110910.jpg',
		'headimage':'user-head/id_00000001.jpg'},

		{'id':2,
		'name':'张小兵',
		'level':13,
		'goodat':['计算机硬件维修','短途物流运送'],
		'image':'id_20110911.jpg',
		'headimage':'user-head/id_00000002.jpg'},
		{'id':3,
		'name':'刘一云',
		'level':11,
		'goodat':['植物修剪','宠物看护','室内保洁'],
		'image':'id_20110913.jpg',
		'headimage':'user-head/id_00000003.jpg'},
		{'id':4,
		'name':'许文昊',
		'level':10,
		'goodat':['LOGO设计','信使服务'],
		'image':'id_20110912.jpg',
		'headimage':'user-head/id_00000004.jpg'}
		]
	employer_list = [
		{'id':1,
		'name':'张菜花',
		'headimage':'user-head/id_00000001.jpg'},
		{'id':2,
		'name':'李黄瓜',
		'headimage':'user-head/id_00000002.jpg'},
		{'id':3,
		'name':'王韭菜',
		'headimage':'user-head/id_00000003.jpg'},
		{'id':4,
		'name':'赵柿子',
		'headimage':'user-head/id_00000004.jpg'}		
	]
	#初始化一段雇主的任务数据
	tasks = Task.objects.filter(is_done=True)[0:5]

	return render_to_response(
		'index.html',{
			'PAGE_TITLE':'首页',
			'tasks_list':tasks,
			'dazatu_list':dazatu_list
		}
	)

		

#it 's a test method for test the server info
def serv_test(request):
	html = []
	for k,v in request.META.items():
		html.append('<div>%s:%s<div>' % (k,v))
	return HttpResponse(html)

#unit test 
if __name__ == '__main__':
	#write some test for unit test
	print('ok!')