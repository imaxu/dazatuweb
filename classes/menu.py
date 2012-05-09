# -*- coding: utf-8 -*-
'''
	CLASS NAME:		Menu
	CREATED DATE:	2011-12-23
	CREATED BY:		xuwh
'''
#=============================================
#菜单基类
#=============================================
class BaseMenu:
	'''顶部菜单基类
	作用：
		提供生成菜单HTML的方法。
	例子：
		请使用派生类。
	'''
	def __init__(self,tag='a',session=None):
		'''构造函数
		args:
			tag - 指定使用的HTML标签，默认值是<a></a>	
		'''
		self.tag = tag
		self.session = session
		self.set_menu_data()
	def get_menu_html(self):
		'''获取生成菜单的HTML
		args:
		return:
			string - 组装好的HTML
		'''
		__html_list = []
		for item in self.menu_data:
			__html_list.append('<%s id=\"%s\" href=\"%s\">%s</%s>' % (self.tag,item[1],item[2],item[0],self.tag,))
		__out = ''.join(__html_list)
		return __out		
	def set_menu_data(self):
		pass

#=============================================
#未登录菜单类，继承自BaseMenu
#=============================================	
class UnLoginedMenu(BaseMenu):
	'''未登陆菜单类
	作用：
		向未登录用户提供菜单HTML
	例子：
		menu = UnloginedMenu()
		menu.get_menu_html()
	'''
	def set_menu_data(self):
		self.menu_data = (
			('登录','menu-0','/user/login/',),
			('注册会员','menu-1','/user/reg/',),
			('申请打杂','menu-2','/user/dazatu/reg/',),
			('了解网站','menu-3','#',),
		)
#=============================================
#已登陆菜单类，继承自BaseMenu
#=============================================		
class LoginedMenu(BaseMenu):
	'''已登陆菜单类
	作用：
		向已登录用户提供菜单HTML
	例子：
		menu = UnloginedMenu()
		menu.get_menu_html()
	'''
	def set_menu_data(self):
		self.menu_data = (
			('登出','menu-0','/user/logout/',),
			('会员中心','menu-1','/user/center/'),
			('申请打杂','menu-2','/user/dazatu/reg/',),
			('了解网站','menu-3','#',),
		)
#=============================================		
#外部调用类
#=============================================
class MenuManager:
	'''菜单的工厂类
	args:
		prefix - 目标类的前缀，可选项包括:
			Logined:返回已登录菜单类；
			UnLogined:返回未登陆菜单类。
		session - 当前访问者的session对象
	'''
	@staticmethod
	def create_menu(prefix=None,session=None):
		__menu_prefix = 'UnLogined'
		if prefix != None:
			__menu_prefix = prefix
		else:
			if session != None and session.get('user_id',0) > 0:
				__menu_prefix = 'Logined'
		__menu = eval('%sMenu' % __menu_prefix)(session=session)
		return __menu
