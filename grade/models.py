from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

# Create your models here.
class user(models.Model):
    user_name = models.CharField(max_length=30)
    pw = models.CharField(max_length=30)
    flag = models.IntegerField(default=1)


#
# class student_admin(admin.ModelAdmin):
#     list_display = ('name','grades')
#
# admin.site.register(student,student_admin)