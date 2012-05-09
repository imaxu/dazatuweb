# -*- coding: utf-8 -*-
from tools.http import set_session,get_is_logined
from users.models import Users
from django.http import HttpResponse
def api_create(request,role,action):
    '''API的工厂方法
        role - 角色
        action - 操作
    '''
    __method = 'api_%s_%s(%s)' % (role,action,request,)
    __func = eval('api_%s_%s' % (role,action,))
    return __func(request)
    
def api_users_set__region(request):
    '''用户角色选择所在区域的API方法
        request - django.HttpRequest对象
        value - 区域的字符串
    '''
    __selected_region = request.POST.get('region','')
    if len(__selected_region) == 0:
        return HttpResponse('') 
    try:
        if get_is_logined(request):
            user = Users.objects.get(id=int(request.session['user_id']))
            if user.user_info_set.all().count() == 0:
                user.user_info_set.create(usually_region=__selected_region)
            else:
                user_info = user.user_info_set.only()[0]
                user_info.usually_region = __selected_region
                user_info.save()
        set_session(request,'region',__selected_region)
        return HttpResponse(__selected_region)
    except:
        return HttpResponse('') 