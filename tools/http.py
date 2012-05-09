# -*- coding: utf-8 -*-
'''
    MODEL NAME:        tools.http
    CREATED BY:        xuwh
    CREATED DATE:    2011-12-19
'''
from django.http import HttpRequest
from tools.log import writelog
def is_exist_in_request(method,key):
    '''判断指定键是否存在与指定的请求数据中
    '''
    if key in method:
        writelog('Func Name:is_exist_in_request;%s in %s.' % (key,method,))
        return True
    return False
#set user session
#request:HttpRequest
#key:session key
#val:session value
#expiry:expiry value,default value is 0
def set_session(request,key,val,expiry=0):
    '''设置指定的session值
        args:
            request -     当前客户端的请求对象
            key     -    session的key键
            val        -    session的值
            expiry    -    session的过期时间，默认为0，即浏览器关闭失效
    '''
    request.session.set_expiry(expiry)
    request.session[key] = val

def get_is_logined(request):
    '''判断当前请求的客户端是否已经登录
    '''
    return get_session_from_key(request,'user_id')>0
    
def get_session_from_key(request,key,default_value=0):
    '''获取当前请求指定KEY的session值
        args:
            request    -    当前客户端的请求对象
            key        -    指定的应当包含在session中的key值
            default_value    -    若指定KEY不存在，则使用的默认值，该参数默认值为0
        return:
            object     -     取决于session内储存的对象类型
    '''
    return request.session.get(key,default_value)

def all_in_request(qd,key_tuple):
    '''判断是否指定的KEY存在于QuerySet
        args:
            qd - 一个QueryDict对象
            key_tuple - 一个储存了key集合的元组
        return:
            boolean - 返回布尔值，指示key_tuple中的值是否都存在于qd中，如果是，返回True
    '''
    return all(k in qd for k in key_tuple)
    
#private function for render a 404 page
#err_action:(action,...) or [action,...]
#err_msg:string
#other_options:{text:url,...} or [(text,url),...]
def render_error_page(err_action,err_msg,other_options,pag_temp='flatpages/404.html'):
    return render_to_response(
        pag_temp,{
            'ERR_ACTION':err_action,
            'ERR_REASONS':err_msg,
            'OTHER_OPTIONS':other_options
        }
    )   