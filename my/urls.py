# -*- coding: utf-8 -*-
"""my URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from werobot.contrib.django import make_view
import grade.views
from wechat.robot import robot
import blog.views, blog.url
import my.settings
import django.views
import xadmin
import ins

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', blog.views.index, name='index'),
    url(r'^blog/', include('blog.url')),
    url(r'^user/', include('blog_user.url')),
    url(r'^comments/', include('django_comments.urls')),

    # url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': my.settings.MEDIA_ROOT}),

    url(r'^grade/',include('grade.url')),   # 用来查成绩
    url(r'^robot/$', make_view(robot)),   # 微信机器人
    url(r'^ins/$', ins.views.index),

# 课程设计
#     url(r'^cj_login/$', s_cj.views.login, name='cj_login'),
#     url(r'^cj/$', s_cj.views.index, name='cj_index'),
#     url(r'^add_student', s_cj.views.add_student, name='add_student'),
#     url(r'^search_course/(?P<id>\d+)/$', s_cj.views.search_course, name='search_course'),
#     url(r'^search_class/(?P<id>\d+)/$', s_cj.views.search_class, name='search_class'),
#     url(r'^search_student/', s_cj.views.search_student, name='serach_s'),
#     # url(r'^delete_sc/(?P<id>\d+)/$', s_cj.views.delete_sc, name='delete_sc'),
#     # url(r'^delete_cno/(?P<id>\d+)/$', s_cj.views.delete_cno, name='delete_cno'),
#     # url(r'^delete_sno/(?P<id>\d+)/$', s_cj.views.delete_sno, name='delete_sno'),
#     url(r'^delete/', s_cj.views.delete, name='delete'),
#     url(r'^update/', s_cj.views.update, name='update'),
]
