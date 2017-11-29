# -*- coding: utf-8 -*-
from django.contrib import admin
import xadmin
from xadmin import views
from blog.models import BlogsPost, Tag
from blog.models import UserProfile
from blog.models import *
from django.contrib.auth.models import User
# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','publish_time', 'update_time', 'read_num', 'tag_list')
    ordering = ('-publish_time',)
    list_filter = ('tag', 'publish_time') #过滤器
    search_fields = ('title', )          #搜索字段
    date_hierarchy = 'publish_time'        #详细时间分层筛选
    filter_horizontal=('tag', )

    def tag_list(self,blog):
        temp = map(lambda x:x.tag_name,blog.tag.all())
        return ','.join(temp)
    # list_editable = ['content','read_num']
    # filter_horizontal = ('tag',)
admin.site.register(BlogsPost,BlogPostAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name','create_time')

admin.site.register(Tag,TagAdmin)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    verbose_name = '用户信息'


class UserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)

# x_admin 设置


class BlogPostAdmin(object):
    list_display = ('title', 'content','publish_time', 'update_time', 'read_num', 'tag_list')
    style_fields = {'content':'ueditor'}
    def tag_list(self, blog):
        temp = map(lambda x: x.tag_name, blog.tag.all())
        return ','.join(temp)


class GlobalSetting(object):
    site_title = '思佳3的后台'
    site_footer = 'sijia3.top'


class TagAdmin(object):
    list_display = ('tag_name', 'create_time')

xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(BlogsPost, BlogPostAdmin)
xadmin.site.register(UserProfile)



