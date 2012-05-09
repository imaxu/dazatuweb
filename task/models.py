# -*- coding: utf-8 -*-
'''
    Model Name:         Users
    Description:
    Created Datetime:    2011-12-15
    Created By:            Xuwh
'''
from django.db import models
from users.models import Users

class Task_Type(models.Model):
    '''任务类别数据对象
    '''
    name = models.CharField(max_length=10,verbose_name='任务类型名称')
    template = models.CharField(max_length=15,verbose_name='任务模板')
    logo = models.CharField(max_length=255,verbose_name='任务的图像标识')
    logo_gray = models.CharField(max_length=255,verbose_name='灰度的任务图像标识')
    
    class Meta:
        db_table = u'da_task_type'

class Task_Manager(models.Manager):
    '''任务数据对象管理类
    '''
    def get_recommend_tasks_or_none(self,start_index=0,size=5):
        '''获取推荐任务列表（无外部条件的）
        '''
        from tools.shortcut import get_time_now
        __start_index = start_index * size
        __now = get_time_now()
        return self.filter(
                            is_done=0,
                            is_assigned=0,
                            assigned_deadline__lte=__now
                        ).order_by('-assigned_deadline')[__start_index:__start_index+size]
    def get_recommend_task_from_clientuser(self,clientuser,task_id=0):
        '''获取基于登录用户的推荐任务集合
        '''
        #TODO:该逻辑非正式逻辑。
        return self.all().exclude(id=task_id)[0:5]
    def get_newest_tasks_or_none(self,start_index=0,size=5):
        '''获取最新的任务列表
        '''
        from tools.shortcut import get_time_now
        __start_index = start_index * size
        __now = get_time_now()
        return self.filter(
                            is_done=0,
                            is_assigned=0,
                            assigned_deadline__lte=__now
                )[__start_index:__start_index+size]
    def get_tasks_from_current_user(self,user=None):
        '''获取当前用户所发布的任务列表
            args:
                user - 当前登录用户的用户数据对象
            return:
                QuerySet - django.queryset
        '''
        return self.filter(user=user)
class Task(models.Model):
    '''任务数据对象
    '''
    title = models.CharField(max_length=24,verbose_name='任务标题')
    describe = models.CharField(max_length=140,verbose_name='任务描述')
    assigned_deadline = models.DateTimeField(null=True,verbose_name='任务分配截止时间')
    finished_deadline = models.DateTimeField(verbose_name='任务完成截止时间')
    private_describe = models.CharField(null=True,max_length=140,verbose_name='任务的非公开信息')
    #locations = models.TextField(verbose_name='任务相关地点描述，可多个，以|分割')
    helper_payment = models.IntegerField(null=True,verbose_name='打杂者需要预先支付的金额')
    is_repeat = models.BooleanField(verbose_name='该任务是否需要重复完成')
    #任务分配模式，分为三种：
    #auto系统自动分配，free雇主自行选择，topfirst在一定周期内系统前5名打杂者有优先选择权周期过后雇主自行选择。
    assignment_type = models.CharField(max_length=8,verbose_name='任务分配模式：auto,free,topfirst')
    is_assigned = models.BooleanField(verbose_name='任务是否已被分配')
    in_region = models.CharField(max_length=16,verbose_name='任务所属区域或城市')
    done_with_virtual = models.CharField(max_length=10,null=True,verbose_name='任务是否可以采用虚拟方式完成，如电话或互联网')
    need_vehicle = models.CharField(max_length=12,null=True,verbose_name='任务是否需要大型的或其他交通工具')
    price = models.IntegerField(verbose_name='用户愿意支付的酬金')
    posttime = models.DateTimeField(verbose_name='任务发布的时间')
    is_done = models.BooleanField(verbose_name='任务是否完成标识')
    task_type = models.ForeignKey(Task_Type)
    user = models.ForeignKey(Users)
    objects = Task_Manager()
    
    def __unicode__(self):
        return '%s' % (self.id,)
    class Meta:
        db_table = u'da_tasks'
        ordering = ['-posttime']
        
class Location(models.Model):
    '''位置信息数据对象
    '''
    name = models.CharField(max_length=255,verbose_name='位置名称')
    province = models.CharField(max_length=12,verbose_name='所属省直辖市地区')
    city = models.CharField(max_length=24,verbose_name='所属市区')
    address = models.CharField(max_length=255,verbose_name='所属县乡或具体地址')
    zip_code = models.CharField(max_length=6,verbose_name='邮编')
    lnt = models.DecimalField(null=True,max_digits=15,decimal_places=11,verbose_name='经度')
    lat = models.DecimalField(null=True,max_digits=15,decimal_places=11,verbose_name='纬度')
    #task = models.ForeignKey(Task)
    user = models.ForeignKey(Users)
    class Meta:
        db_table = u'da_locations'
        
class Task_Location(models.Model):
    task = models.ForeignKey(Task)
    location = models.ForeignKey(Location)
    
    class Meta:
        db_table = u'da_task_location'
