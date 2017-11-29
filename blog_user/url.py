# -*- coding: utf-8 -*-
from django.conf.urls import url
import blog_user.views

urlpatterns = [
    url(r'^$', blog_user.views.login, name='blog_login'),
    url(r'^login/$', blog_user.views.login, name='blog_login'),
    url(r'^login_ajax/$', blog_user.views.login_ajax, name='blog_login_ajax'),
    url(r'^login_out/$', blog_user.views.login_out, name='blog_login_out'),
    url(r'^register/$', blog_user.views.register, name='blog_register'),
    url(r'^imformation/$', blog_user.views.user_imformation, name='user_imfor'),
    url(r'^name_change/$', blog_user.views.username_change, name='name_change'),
    url(r'^password_change/$', blog_user.views.password_change, name='password_change'),
    url(r'^password_lost/$', blog_user.views.password_lost, name='password_lost'),
]