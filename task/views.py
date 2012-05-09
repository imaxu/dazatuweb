# -*- coding: utf-8 -*-
'''
    VIEWS NAME:        user.views
    CREATED BY:        xuwh
    CREATED DATE:    2011-12-16
    UPDATE DATE: 2012-05-10
'''
from django.http import HttpResponse
from django.shortcuts import render_to_response
from tools.http import get_is_logined,get_session_from_key,all_in_request
from tools.shortcut import wrapped_render_to_response
from task.models import Task
from task.models import Task_Type
from users.models import Users

def task_list(request,cur_page=0,get_header=None):
    from classes.widgets import get_tasks
    from settings import TASK_LIST_PAGE_SIZE
    __cur_page = int(cur_page) - 1
    __all_count = Task.objects.all().count()
    return render_to_response(
        'task/list.html',
        {
            'HEADER_MENU':get_header(session=request.session),
            'RECOMMEND_TASKS':get_tasks(
                                        task_function='get_recommend_tasks_or_none',
                                        start_index=__cur_page,
                                        page_size=TASK_LIST_PAGE_SIZE
                            ),
            'NEWEST_TASKS':get_tasks(
                                        task_function='get_newest_tasks_or_none',
                                        start_index=__cur_page,
                                        page_size=TASK_LIST_PAGE_SIZE
                            ),
            'IS_LOGINED':get_is_logined(request),
            #第一个参数是总记录数；第二个参数是当前页
            'RECOMMEND_TASKS_PAGE_NAV':'(%s,%s,)' % (__all_count,__cur_page+1),
            'NEWEST_TASKS_PAGE_NAV':'(%s,%s,)' % (__all_count,__cur_page+1)
        }
    )
    
def task_details(request,task_id=0,get_header=None):
    if task_id > 0:
        __user_id = get_session_from_key(request,'user_id')    
    #try:
        __task = Task.objects.get(id=task_id)        
        if __user_id > 0:
            __current_user = Users.objects.get(id=__user_id)
            __recommend_tasks = Task.objects.get_recommend_task_from_clientuser(__current_user,task_id=task_id)
        else:
            __recommend_tasks = Task.objects.filter(task_type = __task.task_type).exclude(id=task_id)
        return render_to_response(
            'task/details.html',
            {
                'HEADER_MENU':get_header(session=request.session),
                'IS_LOGINED':get_is_logined(request),
                'TASK':__task,
                'RECOMMEND_TASKS':__recommend_tasks
            }
        )
    #except:
        return HttpResponse('您查询的任务不存在。#1')
    else:
        return HttpResponse('您查询的任务不存在。#2')
        
def task_post(request,get_header=None):
    
    if request.method == 'POST':
        if all_in_request(request.POST,('task-type','task-repeat-frequency','task-assign-model',)):
            __queryDataSet = request.POST
            __task_type_id = __queryDataSet['task-type']
            __task_repeat_freq = __queryDataSet['task-repeat-frequency']
            __task_assign_model = __queryDataSet['task-assign-model']
            task_type = Task_Type.objects.get(id=__task_type_id)
            return wrapped_render_to_response(
                'task/post.html',
                {
                    'IS_POSTBACK':True,
                    'HEADER_MENU':get_header(session=request.session),
                    'IS_LOGINED':get_is_logined(request),
                    'TASK_TYPE':task_type,
                    'REQUEST':{
                                'task_repeat_freq':__task_repeat_freq,
                                'task_assign_model':__task_assign_model
                            }
                }
            )
        else:
            return HttpResponse("wrong#")
        
    else:
        return wrapped_render_to_response(
            'task/post.html',
            {
                'IS_POSTBACK':False,
                'HEADER_MENU':get_header(session=request.session),
                'IS_LOGINED':get_is_logined(request),
                'TASK_TYPE':Task_Type.objects.get(id=3)#默认任务类型为其他
            }
        )        
def task_post_review(request,get_header=None):
    task = Task()
    task.title = request.POST['task_title']
    task.describe = request.POST['task_describe']
    task.private_describe = request.POST['task_private_describe']
    task.price = request.POST['task_price']
    task.helper_payment = request.POST['task_helper_payment']
    task.task_type = Task_Type.objects.get(id=request.POST['task_type'])
    task.private_describe = request.POST['task_private_describe']
    return wrapped_render_to_response(
        'task/post_review.html',
        {
            'HEADER_MENU':get_header(session=request.session),
            'TASK':task
        }
    )
def task_post_widget(request):
    if 'widget_name' in request.POST:
        widget_name = request.POST['widget_name']
        __args = {k.upper():request.POST[k] for k in request.POST.keys()}
        return render_to_response(
            'task/task-post-widget-%s.html' % (widget_name,),
            eval('__get_%s_dict(**%s)' % (widget_name,__args))
        )


def __get_step1_dict(**args):
    from task.models import Task_Type
    args['TASK_TYPES']= Task_Type.objects.all()#加入所有任务集合
    return  args
