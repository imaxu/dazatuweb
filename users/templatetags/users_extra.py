# -*- coding:utf-8 -*-
from django import template
from users.models import Users,User_Info
register = template.Library()

@register.filter
def get_user_headimage_from_user(user):
	from settings import USER_HEAD_IMAGE_DIR
	try:
		__user_info = User_Info.objects.get(user=user)
		__head_img = '%s%s' % (USER_HEAD_IMAGE_DIR,__user_info.header_image_path,)
	except:
		__head_img = '%suser_img_default.jpg' % (USER_HEAD_IMAGE_DIR,)
	finally:
		return __head_img
	