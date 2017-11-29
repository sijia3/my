# -*- coding: utf-8 -*-
from django.conf.urls import url,include
import grade.views

urlpatterns = [
    url(r'^$', grade.views.login_user, name='grade_login'),
    url(r'^', grade.views.cj),          # 成绩查询登陆跳转页面
]