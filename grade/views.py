# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from login import fosu100net
# Create your views here.5555qq
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def login_user(request):
    if request.method == 'POST':
        global user, pw
        user = str(request.POST.get('user'))        # 只能用一次，，，如何解决
        pw = str(request.POST.get('pw'))
        try :
            if fosu100net.check_is_login(user, pw):
                return HttpResponseRedirect('/grade/'+user)        # 重定向到成绩显示页面
            else:
                return render(request, 'login.html', {"error" : "账号或密码出错，请重新输入!!"})
        except:
            return render(request, 'login.html', {"error" : "嘻嘻100网炸了!!"})
    return render(request, 'login.html')
# YEHL1426468134


def cj(request):
    # NameError
    try :
        data = dict()
        data['grade_list'], data['xuefenji'] = fosu100net.get_student_grade()                # 学生成绩的所有信息
        data['user_information'] = fosu100net.get_student_information()    # 学生个人信息
        for i in data['user_information'].values():
            print i,
        print "\n"
        if not data['grade_list']:
            data['empty'] = "你大概还是新生吧，还没查到任何成绩哈！"
        return render(request, 'cj.html', data)
    except:
        data['flag'] = False
        return render(request, 'cj.html', data)