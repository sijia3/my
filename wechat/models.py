# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

# Create your models here.
class student(models.Model):
    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'
    open_id = models.CharField('微信id',max_length=30)
    name = models.CharField('姓名',max_length=30)
    xuehao = models.CharField('学号',max_length=30)
    def __str__(self):
        return self.name
        # return u'%s %s'%(self.name,self.xuehao)
class grade(models.Model):
    class Meta:
        verbose_name = '学生成绩'
        verbose_name_plural = '学生成绩'
    student = models.ForeignKey(student,related_name='s_grade',verbose_name="学生")    #一对多的关系。可以是一个学生对应多个成绩表，例如期中成绩和期末成绩
    yuwen = models.CharField('语文',max_length=30)
    shuxue  = models.CharField('数学',max_length=30)
    yingyu = models.CharField('英语',max_length=30)
    zonghe = models.CharField('综合',max_length=30)
    def __str__(self):
        # return u'%s %s'%(self.s.name,self.s.xuehao)
        return self.student.name