# coding=utf-8
from django.core.urlresolvers import reverse
from blog.models import BlogsPost
from blog.models import Tag
from blog.models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
import time
import json
from blog.views import th
# Create your views here.


def login(request):
    data = {}
    data["tags"] = th.get_information(None)
    return render_to_response('blog_login(1).html', data, context_instance=RequestContext(request))

def login_ajax(request):
    data = {}
    try:
        if request.method == 'POST':
            username = (request.POST.get('username'))
            password = (request.POST.get('password'))
            user = authenticate(username=username, password=password)
            print username, password, user
            if user is not None:
                auth_login(request, user)
                data["flag"] = True
            else:
                data["flag"] = False
    except Exception:
        pass
    print data
    return HttpResponse(json.dumps(data), content_type='application/json')


def login_out(request):
    auth_logout(request)
    return HttpResponseRedirect('/blog')   # request.META.get('HTTP_REFERER', '/')


def register(request):
    data = dict()
    data["tags"] = th.get_information(None)
    if request.method == 'POST':     # 异步传输。。
        imf = {}
        username = (request.POST.get('username'))
        password1 = (request.POST.get('password1'))
        password2 = (request.POST.get('password2'))
        user = User.objects.filter(username=username)
        if user:
            imf["flag"] = "name"
            return HttpResponse(json.dumps(imf), content_type='application/json')
        if password1 != password2:
            imf["flag"] = "pwd"
            return HttpResponse(json.dumps(imf), content_type='application/json')
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        profile = UserProfile()
        profile.user_id = user.id
        profile.save()
        imf["flag"] = "yes"
        user = authenticate(username=username, password=password1)
        if user is not None:
            auth_login(request, user)
        return HttpResponse(json.dumps(imf), content_type='application/json')
    return render_to_response('blog_register(1).html', data, context_instance=RequestContext(request))


def check_is_login(func):
    data = dict()
    def warpper(request):
        if request.user.is_authenticated():
            result = func(request)
        else:
            # result = HttpResponseRedirect('/blog')     # 还没提示直接跳转
            data['flag'] = True
            data['tips'] = "大佬你还没登录。三秒后自动跳转。"
            result = render_to_response('404.html', data)
        return result
    return warpper


@check_is_login
def user_imformation(request):
    data = dict()
    data["tags"] = th.get_information(None)
    data['user_image'] = "http://119.29.243.188/media/"+str(request.user.get_avatar_url())
    return render_to_response('user_imformation(1).html', data, context_instance=RequestContext(request))


@check_is_login
def username_change(request):
    user = request.user
    data = dict()
    if request.method == "POST":
        u_name = request.POST.get('username')
        user.username = u_name
        if User.objects.filter(username=u_name):
            data['error'] = "用户名存在！！"
            return render_to_response('username_change(1).html', data, context_instance=RequestContext(request))
        user.save()
        data['error'] = "修改成功！！"
        return render_to_response('username_change(1).html', data, context_instance=RequestContext(request))
    return render_to_response('username_change(1).html', data)


@check_is_login
def password_change(request):
    user = request.user
    data = dict()
    data["username"] = user.username
    data["password"] = user.password
    if request.method == "POST":
        u_password = request.POST.get('password')
        user.set_password(u_password)
        user.save()
        user = authenticate(username=user.username, password=u_password)   # 重新登录帐号
        auth_login(request, user)
        return HttpResponseRedirect('/blog', time.sleep(3))
    return render_to_response('password_change(1).html', data)


@check_is_login
def password_lost(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        user = User.objects.get(username=username)
        if user:
            user.set_password(password1)
            user.save()
            user = authenticate(username=user.username, password=password1)   # 重新登录
            auth_login(request, user)
            data['error'] = "密码重置完成，正在为你跳转。。"
            return HttpResponseRedirect('/blog', time.sleep(3))
        return render_to_response('password_lost(1).html', data, context_instance=RequestContext(request))
    return render_to_response('password_lost(1).html', data)