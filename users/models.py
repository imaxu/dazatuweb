# -*- coding: utf-8 -*-
'''
	Model Name: 		Users
	Description:
	Created Datetime:	2011-12-15
	Created By:			Xuwh
'''
from django.db import models



#***********************************************************************
#Users：有关用户基本信息与使命身份信息的数据对象
#***********************************************************************
#=============================================
#Users的管理类，继承自models.Manager
#=============================================	
class Users_Manager(models.Manager):

	def exist_any(self,id_no,email,mobile_phone):
		return False


#=============================================
#Users Model
#=============================================			
class Users(models.Model):
	first_name = models.CharField(max_length=8,verbose_name='用户姓氏')
	last_name = models.CharField(max_length=8,verbose_name='用户名字')
	appellation = models.CharField(max_length=12,verbose_name='用户的称谓，用于隐藏名字')
	password = models.CharField(max_length=32,verbose_name='用户密码MD5_32')
	id_no = models.CharField(max_length=18,unique=True,verbose_name='用户个人身份证号')
	email = models.EmailField(unique=True,verbose_name='用户电子邮箱地址')
	mobile_phone = models.CharField(max_length=15,unique=True,verbose_name='用户移动电话号码')
	is_real_validate = models.BooleanField(verbose_name='指示是否通过了实名验证')
	#override Users.objects
	objects = Users_Manager()
	
	def __unicode__(self):
		return u'%s %s'.decode('utf-8') % (self.first_name,self.last_name)
	class Meta:
		db_table = u'da_users'
		
#***********************************************************************
#Users END
#***********************************************************************		
#***********************************************************************
#User_Info：有关用户扩展信息的数据对象
#***********************************************************************

#=============================================
#User_Info的管理类，继承自models.Manager
#=============================================	
class User_Info_Manager(models.Manager):
	def get_user_info_complete(self,user=None):
		'''获取用户信息完成度数值
		args:
			user_id - 用户ID，默认值为0
		return:
			float - 返回0-1之间的浮点数，返回1为100%完成度，0为0%
		'''
		try:
			
			u_info = self.get(user=user)
			__ret = 0
			if u_info.national != None and len(u_info.national) > 0:
				__ret = __ret + 0.1
			if u_info.usually_region != None and len(u_info.usually_region) > 0:
				__ret = __ret + 0.2
			if u_info.header_image_path != None and len(u_info.header_image_path) > 0:
				__ret = __ret + 0.3			
			if u_info.usually_addresses != None and len(u_info.usually_addresses) > 0:
				__ret = __ret + 0.2
			return __ret
		except:
			return 0.0
#=============================================
#User_Info Model
#=============================================	
class User_Info(models.Model):
	national = models.CharField(null=True,max_length=2,verbose_name='国籍')
	usually_region = models.CharField(null=True,max_length=255,verbose_name='经常所在地，格式：省，市，区')
	usually_addresses = models.TextField(null=True,verbose_name='常用的地址，最多5个，格式：XXXX,XXXX|XXXXX,XXXX')
	header_image_path = models.CharField(max_length=225,null=True,verbose_name='用户头像文件名')
	user = models.ForeignKey(Users)
	
	objects = User_Info_Manager()
	class Meta:
		db_table = u'da_User_Info'
		
#***********************************************************************
#User_Info END
#***********************************************************************
	
	


	
