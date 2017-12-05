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
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', blog.views.index, name='index'),
    url(r'^blog/', include('blog.url')),
    url(r'^user/', include('blog_user.url')),
    url(r'^comments/', include('django_comments.urls')),

    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': my.settings.MEDIA_ROOT}),

    url(r'^grade/',include('grade.url')),   # 用来查成绩
    url(r'^robot/$', make_view(robot)),   # 微信机器人
    # url(r'^plist/$', blog.views.helloParams),
]
