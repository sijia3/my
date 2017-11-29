# coding=utf-8
# from django.shortcuts import render
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
# Create your views here.


class TagsHelper:            # 标签辅助类
    def __init__(self):
        self.tags = Tag.objects.all()
        self.count = len(self.tags)

    def get_information(self, tag_list):  # 获取所有的标签进行显示
        tag_blog = []
        for i in Tag.objects.all():
            t = dict()
            t['id'] = i.id
            t['tag_name'] = i
            t['num'] = len(i.t_blog.all())
            if tag_list is not None:
                if str(i.id) in tag_list:
                    t['check'] = True
            else:
                t['check'] = False
            tag_blog.append(t)
        return tag_blog

    def get_blog_tags(self, id):     # 获取单个博客文章的所有标签
        blog_to_tags = []
        blog = BlogsPost.objects.get(id=id)
        tagged = blog.tag.all()
        for i in tagged:
            t = dict()
            t['id'] = i.id
            t['tag_name'] = i
            t['num'] = len(i.t_blog.all())
            blog_to_tags.append(t)
        return blog_to_tags

th = TagsHelper()    # 实例化


# 页码辅助函数
def get_pages(request, object_lists):
    current_page = request.GET.get('page', 1)     # 获得当前页数，默认为1
    paginator = Paginator(object_lists, 7)         # 得到一个分页后的对象
    object_lists = paginator.page(current_page)   # 得到当前页面的blog列表
    current = object_lists.number
    page_all = paginator.num_pages
    page_range = []
    if page_all < 5:
        page_range = paginator.page_range
    else:
        page_range += [1, page_all]
        page_range += [current-1, current, current+1]
        if current == 1 or current == page_all:
            page_range += [current+2, current-2]

        # 去掉超出范围的页码
        page_range = filter(lambda x: 1 <= x <= page_all, page_range)

        # 排序去重
        page_range = sorted(list(set(page_range)))
        t = 1             # 这是一个坑
        for i in range(1, len(page_range)):
            # print page_range[i],page_range[i-1]
            if page_range[t]-page_range[t-1] > 1:
                page_range.insert(t, '...')
                # print page_range
                t += 1
            t += 1
        # print page_range
    paginator.page_range_ex = page_range    # 创建一个paginator的属性page_range_ex
    return object_lists, paginator


def index(request):
    data = {}
    tag_list = request.GET.getlist('tag')
    # 按时间排序
    if tag_list:               # 如果有选择标签，就做着件事
        blogs = BlogsPost.objects.filter(tag__in=tag_list).order_by('-id')
        blogs = blogs.distinct()
    else:
        blogs = BlogsPost.objects.all().order_by('-id')
    blogs, pages = get_pages(request, blogs)

    data['tag_list'] = tag_list
    data["blogs"] = blogs
    data["pages"] = pages       # 总页码数
    data["tags"] = th.get_information(tag_list)

    if request.user.is_authenticated():
        data['username'] = request.user
        data['user_image'] = "http://119.29.243.188/media/"+str(request.user.get_avatar_url())
        # print request.user.get_avatar_url()

    return render_to_response('index - 副本.html', data, context_instance=RequestContext(request))


def blog_show(request, id):
    data = dict()
    blog = BlogsPost.objects.get(id=id)
    data['tagged'] = th.get_blog_tags(id)
    blog.read_num += 1
    blog.save()
    data['blog'] = blog
    pre_blog = BlogsPost.objects.filter(id__gt=blog.id).order_by('id')
    next_blog = BlogsPost.objects.filter(id__lt=blog.id).order_by('-id')

    # 取第1条记录
    if pre_blog.count() > 0:
        data['pre_blog'] = pre_blog[0]
        data['pre_blog_abstract'] = pre_blog[0].title
    else:
        data['pre_blog'] = None

    if next_blog.count() > 0:
        data['next_blog'] = next_blog[0]
        data['next_blog_abstract'] = next_blog[0].title
    else:
        data['next_blog'] = None
    data["tags"] = th.get_information(None)
    if request.user.is_authenticated():
        data['user_image'] = "http://119.29.243.188/media/"+str(request.user.get_avatar_url())
    return render_to_response('blog_show.html', data, context_instance=RequestContext(request))


def search(request):
    data = {}
    current_tag = request.GET.get('tag')
    key = request.GET['key']
    if not key:
        return index(request)
    blogs = BlogsPost.objects.filter(title__contains=key)
    if not blogs:
        data['tips'] = '请重新输入关键字。'
        return render_to_response('404.html',data)
    blogs, pages = get_pages(request, blogs)
    if current_tag:               # 如果有这个标签
        tag = Tag.objects.filter(id=current_tag)
        blogs = tag[0].t_blog.all()
        data["current_tag"] = current_tag       # 增加标签的tag，使多页page能正常显示
    data['blogs'] = blogs
    data['pages'] = pages
    data["tags"] = th.get_information(None)
    data['key'] = key
    return render_to_response('blog_search(1).html', data, context_instance=RequestContext(request))


def editor(request):
    data = dict()
    data['tags'] = th.get_information(None)
    return render_to_response('blog_editor.html', data, context_instance=RequestContext(request))


def editor_ajax(request):
    data = dict()
    try:
        if request.method == "POST":
            blog_title = request.POST.get('blog_title')  # 获取标题
            blog_tags = request.POST.getlist('tag')  # 获取分类标签的列表
            blog_content = request.POST.get('content')  # 获取正文内容
            tag_ids = []
            for tag in blog_tags:
                    tag_id = int(tag)
                    tag_ids.append(tag_id)
            blog = BlogsPost()
            blog.title = blog_title
            blog.content = blog_content
            blog.save()
            for tag in Tag.objects.filter(id__in=tag_ids):
                blog.tag.add(tag)
            # 返回结果
            data['success'] = True
            data['message'] = reverse('detailblog', args=[blog.id, ])
    except Exception as e:
            data['success'] = False
            data['message'] = e.message

    return HttpResponse(json.dumps(data), content_type='application/json')


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



