# -*- coding: utf-8 -*-
from django import template

register = template.Library()

#过滤器定义
@register.filter
def print_page_nav(value,arg):
    '''根据参数拼装并输出分页导航HTML代码
        args:
            value     -     该参数为一个包含2个元素的元组，(总记录数,当前页码,)
            arg     -     该参数为字典，基本元素包含{link:value,pagesize:value,addtion:value}
                        其中：
                            link表示链接地址，
                            pagesize表示每一页显示多少条数据,
                            addtion传入附加内容，该附加内容将被添加至链接地址尾部
        return:
            string     -    拼装好的HTML代码
                        
    '''
    from settings import TASK_LIST_PAGE_SIZE
    arg = eval(arg)
    value = eval(value)
    __addtion = arg.get('addtion','')
    __count = value[0]        #读取总记录数
    __cur_page = value[1]    #读取当前页序号
    __link = arg.get('link','')        #读取指定的链接，默认为''，同当前页
    __tag = 'a'                        #指定HTML标签
    __page_size = arg.get('pagesize',TASK_LIST_PAGE_SIZE)        #读取每页显示多少条数据，默认10
    __html = []
    __pages = abs(__count / -(__page_size))
    for i in range(1,__pages+1):
        if i==__cur_page:
            __html.append(
                '<a class=\"page_nav_curr\">%s</a>' % (i,)
            )
            continue
        __html.append(
            '<%s href=\"%s%s/%s\">%s</%s>' % (__tag,__link,i,__addtion,i,__tag,)
        )
    return ''.join(__html)
@register.filter
def get_task_elapsed_times(value):
    from tools.shortcut import get_timedelta_between_timestr,get_seconds_from_timedelta
    __timedelta = get_timedelta_between_timestr(time_str1=value)
    __sec = get_seconds_from_timedelta(timedelta=__timedelta)
    # if __sec shorter than 1 hour
    if __sec < 3600:
        return '%s分钟前' % (__sec / 60,)
    # if __sec longer than 1 hours and shorter than 1 day
    if __sec >= 3600 and __sec < 86400:
        return '%s小时前' % (__sec / 3600,)
    # if __sec longer than 1days
    if __sec >= 86400 :
        return '%s天前' % (__sec / 86400,)
    # if all missed
    return '很久以前'
@register.filter
def get_locations_from_task(task):
    '''获取当前任务的位置信息
    '''
    task_location_relates = task.task_location_set.all()
    locations = [task_location.location for task_location in task_location_relates]
    return locations
    
@register.filter
def get_single_location_from_task(task):
    '''返回指定任务的第一个位置数据
    '''
    __locations = get_locations_from_task(task)
    if len(__locations) > 0 :
        return __locations[0]
    return None
    
@register.filter
def get_singel_location_to_mapsearch(task):
    '''获取单个location，并返回对地图搜索友好的关键字
    '''
    __location = get_single_location_from_task(task)
    if __location != None:
        return '%s %s' % (__location.city,__location.address,)
    return ''
    
@register.filter
def get_logo_url_from_tasktype(task_type):
    '''获取task_type的图标路径，该路径相对于/static/目录
         args:
            task_type - 任务类型对象
        return:
            string - 相对于/static/路径字符串
    '''
    from settings import TASK_TYPE_LOGO_DIR
    return '%s%s' % (TASK_TYPE_LOGO_DIR,task_type.logo,)
@register.filter	
def get_friend_assignmodel_from_code(code):
	'''获取友好的分配模式字符串
	'''
	__prefix = {
		'auto':'系统自动将任务分配给打杂兔。',
		'free':'由您来选择和邀请打杂兔。',
		'topfirst':'顶级打杂兔优先权模式。'
	}
	return __prefix.get(code,'默认')
#标签定义
