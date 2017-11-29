# -*- coding: utf-8 -*-
import werobot
import requests
from wechat.models import  student
from wechat.models import grade
import re
from grade.login import get_messages
robot = werobot.WeRoBot(token = '1234')

@robot.handler
def text_handler(message):
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : 'eb720a8970964f3f855d863d24406576',
        'info'   : message.content,
        'userid' : 'wechat-robot',
    }
    r = requests.post(api_url,data = data).json()
    print message.source
    return r['text']

@robot.filter("成绩")
def a(message,session):

    s = student.objects.filter(open_id=message.source)
    if s:
        # id = student.objects.get(open_id=message.source).id
        # pw = student.objects.get(open_id=message.source).grades
        # list = get_messages.get_user_information(name,pw)
        # str = list['xh']+"\n"+list['xm']
        # return str
        st1 = student.objects.get(open_id=message.source)
        g = st1.s_grade.all()
        # g = st1.grade_set.all()
        print g[0].yuwen
        return student.objects.get(open_id=message.source).name
    else:
        # return "请输入学号+密码绑定。"
        return "请输入班级座号+你的名字进行绑定（如：姓名+李三）"      #应该修改绑定学生姓名跟座位号。  学生信息一个表，学生成绩一个表，如何

@robot.filter(re.compile(".*?\+.*?"))
def b(message):
    #将数据存进数据库
    # student.objects.create(open_id=message.source,name=message.content[3:])
    # [0:2]是班级座号
    student.objects.filter(name=message.content[3:]).update(open_id=message.source)
    return '绑定好了。'




robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
# robot.run()
