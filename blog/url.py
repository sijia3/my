# -*- coding: utf-8 -*-
from django.conf.urls import url,include
import blog.views

urlpatterns = [
    url(r'^$', blog.views.index, name='index'),
    url(r'^(?P<id>\d+)/$', blog.views.blog_show, name='detailblog'),
    url(r'^search/$', blog.views.search, name='search'),

    url(r'^editor/$', blog.views.editor, name='editor'),
    url(r'^editor_ajax/$', blog.views.editor_ajax, name='editor_ajax'),    # 写处理文章提交的内容，没有返回模板

]
