# -*- coding: utf-8 -*-
'''
'''

def get_header(prefix=None,session=None):
	from classes.menu import MenuManager
	return MenuManager.create_menu(
		prefix=prefix,
		session=session
	).get_menu_html()
	
def get_tasks(task_function='get_newest_tasks_or_none',start_index=0,page_size=10):
	from task.models import Task
	return eval('Task.objects.%s(%s,%s)' % (task_function,start_index,page_size,))
	#return Task.objects.get_newest_tasks_or_none(start_index,page_size)