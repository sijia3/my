# -*- coding: utf-8 -*-
from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import User

from DjangoUeditor.models import UEditorField

from types import MethodType
# Create your models here.


class Tag(models.Model):
    """博客分类"""
    class Meta:
        verbose_name = '博客标签'
        verbose_name_plural = '博客标签'
    tag_name = models.CharField('标签类型', max_length=20)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.tag_name


class BlogsPost(models.Model):
    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'
    title = models.CharField('标题', max_length=50)
    # author = models.ForeignKey()
    tag = models.ManyToManyField(Tag, related_name="t_blog")
    content = UEditorField('内容', height=100, width=500)
    publish_time = models.DateTimeField('创建时间',auto_now_add="true")
    update_time = models.DateTimeField('更新时间', auto_now="true")
    read_num = models.IntegerField('阅读次数', default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='user_image')

    def __str__(self):
        return self.user.username
    # address = models.CharField(max_length=100)


def get_avatar_url(self):
    try:
        avatar = UserProfile.objects.get(user=self.id)
        if avatar.avatar:
            return avatar.avatar
        else:
            return 'user_image/user-male-icon.png'
    except Exception as e:
        return 'user_image/user-male-icon.png'

# 动态绑定方法
User.get_avatar_url = MethodType(get_avatar_url, None, User)


