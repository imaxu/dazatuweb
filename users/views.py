# -*- coding: utf-8 -*-
'''
    VIEWS NAME:        user.views
    CREATED BY:        xuwh
    CREATED DATE:    2011-12-16
'''
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404

from models import Users,User_Info
from tools.http import is_exist_in_request,set_session,get_is_logined,all_in_request,render_error_page
from tools.log import writelog
# user/reg page views
def user_reg(request,get_header=None):
    req_method = request.method
    title_dict = {
        'POST':'继续申请新帐号',
        'GET':'开始申请新帐号'
    }
    tag_dict = {
        'PAGE_TITLE':title_dict.get(req_method,'申请新帐号'),
        'U_EMAIL':request.REQUEST.get('em',''),
        'HEADER_MENU':get_header(
                        session=request.session
                    )
    }
    return _user_reg_render(tag_dict)
#private function:render user/reg.html to client
def _user_reg_render(tagdict):
    return render_to_response(
        'user/reg.html',
        tagdict
        )
        
def _makemd5(str):
    import hashlib
    return hashlib.md5(str).hexdigest().upper()
#user/reg/post views
def user_reg_post(request):
    if all_in_request(request.POST,('fname','lname','appe','email','password','idcard','mphone',)):
        _first_name = request.POST['fname']
        _last_name = request.POST['lname']
        _password = request.POST['password']
        _appellation = request.POST['appe']
        _email = request.POST['email']
        _id_no = request.POST['idcard']
        _mobile_phone = request.POST['mphone']    
        # validate user's info if that exist
        has_exist_any = Users.objects.exist_any(_email,_id_no,_mobile_phone)        
        if not has_exist_any:
            #make a md5 password
            _password = _makemd5(_password)
            #make md5 END
            
            #init a new user obj
            new_user = Users(
                first_name=_first_name,
                last_name=_last_name,
                password=_password,
                appellation=_appellation,
                email=_email,
                id_no=_id_no,
                mobile_phone=_mobile_phone)
            # init new user obj END 
            
            try:
                # try to save new user obj
                new_user.save()    
                #record session
                set_session(request,'user_id',new_user.id)
                #向客户端响应包含新用户姓氏，称谓以及ID的HTML代码
                return render_to_response(
                    'user/reg_success.html',{
                        'U_FIRST_NAME':new_user.first_name,
                        'U_APPELLATION':new_user.appellation,
                        'U_ID':new_user.id
                    }
                )
            except Exception:
                import sys
                ex = sys.exc_info()[2].tb_frame.f_back
                writelog('**Exception:%s on line %s' %(ex.f_code.co_name,ex.f_lineno,))
                return render_error_page(
                            err_action='我们在提交注册申请时',
                            err_msg=(
                                '服务器访问量太大，暂时无法响应您的请求。',
                            ),
                            other_options=[('回到打杂兔网站首页','/',),('挺稍后再尝试注册','/user/reg/',)]
                        )
        else:
            return render_error_page(
                        err_action='我们在提交注册申请时',
                        err_msg=(
                            '您提交的电子邮箱已经被注册。',
                            '您提交的身份证件号码已经被注册。',
                            '您提交的手机号码已经被注册。',
                        ),
                        other_options=[('回到打杂兔网站首页','/',),('重新注册','/user/reg/',)]
                    )
    else:
        return render_error_page(
            '您在访问本页时',
            ('您没有使用正确的浏览方式访问本页。',),
            [('回到打杂兔网站首页','/',)])
#user/reg/validate views
#validate user post info ,
#it will return 1 if validation passed
def user_reg_validate(request):
    if 'email' in request.POST:
        #validate user email data
        # if QuerySet has more than one records,
        # then there is a same email address in DB
        if (Users.objects.filter(email=request.POST['email']).count() > 0):
            return render_error_page(
                        err_action='我们在验证电子邮件地址时',
                        err_msg=('您所提交的电子邮件地址已经注册过，一个地址只允许绑定一个帐号。',),
                        other_options=[('点击右上角的关闭按钮，修改电子邮件地址。','#',)])
        return HttpResponse("1")
    elif 'idcard' in request.POST and 'mphone' in request.POST:
        #validate user id_card number and mobile_phone number
        if (Users.objects.filter(id_no=request.POST['idcard']).count() > 0):
            return render_error_page(
                        err_action='我们在验证您的身份证件时',
                        err_msg=('您所提交的身份证号码已经注册过，每个号码只能注册一次。',),
                        other_options=[
                            ('点击右上角的关闭按钮，修改身份证号。','#',),
                            ('致电网站，进行申诉：010-00000000','#',),
                            ('联系在线客服QQ：000000','#',)
                        ]
                    )
        if (Users.objects.filter(mobile_phone=request.POST['mphone']).count() > 0):
            return render_error_page(
                        err_action='我们在验证您的手机号码时',
                        err_msg=('您所提交的手机号码已经注册过，每个号码只能注册一次。',),
                        other_options=[
                            ('点击右上角的关闭按钮，修改手机号码。','#',),
                            ('致电网站，进行申诉：010-00000000','#',),
                            ('联系在线客服QQ：000000','#',)
                        ]
                    )    
        #1 means that's successfull
        return HttpResponse("1")        
    else:
        #unknown visit
        raise Http404()    
#user/center views
def user_center(request,get_header=None):
    if get_is_logined(request) == False:
        return render_error_page(
                    pag_temp='flatpages/404-full.html',
                    err_action='您在访问本页时',
                    err_msg=(
                        '您长时间没有操作需要重新登陆。',
                        '您还没有登陆，因此我们不能向您提供本页内容。'
                    ),
                    other_options=[
                        ('立刻登陆到打杂兔网站','/user/login/',),
                        ('现在注册成为打杂兔会员','/user/reg/',),                    
                        ('回到打杂兔网站首页','/',)
                    ]
                )
    else:
        uid = request.session['user_id']
        from task.models import Task
        __user = Users.objects.get(id=uid)
        return render_to_response(
                'user/center.html',
                {
                    'HEADER_MENU':get_header(session=request.session),
                    #计算当前用户的信息完成度
                    'USER_INFO_COMPLETE':int(User_Info.objects.get_user_info_complete(user=__user) * 100),
                    'RECOMMEND_TASKS':Task.objects.get_recommend_tasks_or_none(0,5),#获取推荐任务列表
                    'NEWEST_TASKS':Task.objects.get_newest_tasks_or_none(0,5),#获取最新任务列表,
                    'CURRENT_USER_TASKS':Task.objects.get_tasks_from_current_user(user=__user),
                    'USER':Users.objects.get(id=uid),
                    'IS_LOGINED':True
                }
            )


def user_login(request,get_header=None):
    dict = {
        'HEADER_MENU':get_header(session=request.session)
    }
    return render_to_response(
        'user/login.html',
        dict
    )

def user_login_validate(request):
    query_dict = request.POST
    get_user_functions = {
        'mobile_phone':_get_user_with_mobile_phone,
        'email':_get_user_with_email
    }
    if query_dict.__contains__('l_account') and query_dict.__contains__('l_password'):
        u_account = query_dict['l_account']
        u_password = _makemd5(query_dict['l_password'])
        try:
            users = get_user_functions[_get_account_type(u_account)](u_account,u_password)
            #user is correctly
            if users.count() == 1:
                set_session(request,'user_id',users[0].id)
                return HttpResponse('%s' % request.session['user_id'])
        except KeyError:
            return HttpResponse('您输入的帐号格式不正确。[#0]')
    return HttpResponse('您输入的帐号或者密码不正确。[#1]')
    
def _get_user_with_email(account,password):
    users = Users.objects.all().filter(email=account,password=password)
    return users
    
def _get_user_with_mobile_phone(account,password):
    users = Users.objects.all().filter(mobile_phone=account,password=password)
    return users
    
#pri function:
#Returns a string
#when it raised a error ,return value is "default"
def _get_account_type(account):
    import re
    re_exprs = (
        (r'^\d{11}$','mobile_phone',),
        (r'([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$','email',),
    )
    for re_expr in re_exprs:
        if re.match(re_expr[0],account) != None:
            return re_expr[1]
    return "default"
    
def user_logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect('/')
       
if __name__ == '__main__'    :
    print('ok')
