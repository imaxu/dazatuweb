# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.conf import settings
from classes.widgets import get_header
#root views
urlpatterns = patterns('',
			# Examples:
			# url(r'^$', 'dazatu_com.views.home', name='home'),
			# url(r'^dazatu_com/', include('dazatu_com.foo.urls')),
			# Uncomment the admin/doc line below to enable admin documentation:
			# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

			# Uncomment the next line to enable the admin:
			# url(r'^admin/', include(admin.site.urls)),	
    url(r'^$', 'views.index', name='index'),
	)
#users views
urlpatterns += patterns('users.views',
    url(r'^user/reg/$', 'user_reg',{'get_header':get_header}),
	url(r'^user/reg/post/$', 'user_reg_post'),
	url(r'^user/reg/validate/$', 'user_reg_validate'),
	url(r'^user/center/$', 'user_center',{'get_header':get_header}),
	url(r'^user/login/$', 'user_login',{'get_header':get_header}),
	url(r'^user/login/validate/$', 'user_login_validate'),
	url(r'^user/logout/$', 'user_logout'),
	)
#tasks views
urlpatterns += patterns('task.views',
    url(r'^task/list/(?P<cur_page>\d*)/$', 'task_list',{'get_header':get_header}),
	url(r'^task/details/(?P<task_id>\d*)/$', 'task_details',{'get_header':get_header}),
	url(r'^task/post/$', 'task_post',{'get_header':get_header}),
	url(r'^task/post/review/$', 'task_post_review',{'get_header':get_header}),
	url(r'^task/post/widget/$', 'task_post_widget'),
	)
	
urlpatterns += patterns('api.views',
    url(r'^api/(?P<role>.*)/(?P<action>.*)/$', 'api_create'),
	)
#static files proccess	
urlpatterns += patterns('',
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.STATIC_ROOT,
	}),	
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.MEDIA_ROOT,
	}),	
	
)
if settings.DEBUG is False:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': settings.MEDIA_ROOT,
		}),			
   )