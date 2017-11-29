# -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from blog.models import BlogsPost
from blog.views import *
from django.test import Client
from selenium import webdriver
import django.utils.timezone as timezone

class Test(TestCase):
    # def test_url(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func,index)
    def test_index_returns_current_html(self):
        # request = HttpRequest()
        # response = index(request)
        # print response
        # self.assertIn(b"<title>sijia3ww' Blog</title>", response.content)
        # respone = self.client.get('/user/imformation/')
        # print respone
        # self.assertIn(b"大佬，你", respone.content)

        response = self.client.post('/', {'username' : "12", 'password' : "12"})
        print response

        def test_can_return_sql_content(self):

            Tag.objects.create(tag_name='人民', create_time=timezone.now())
            Tag.objects.create(tag_name='青春', create_time=timezone.now())
            first_blog = BlogsPost()
            first_blog.title = "ddd"
            first_blog.content = "ffefs"
            first_blog.save()
            # first_blog.tag = [Tag.objects.all()[0]]
            # print first_blog.tag.all()
            # for i in t:
            #     print i.id
            tag_ids = [1,2]
            for tag in Tag.objects.filter(id__in=tag_ids):
                # print tag.id,tag.tag_name,tag.create_time
                first_blog.tag.add(tag)
            print first_blog.tag.all()
            response = self.client.get('/')
            # print response
            self.assertIn("<title>sijia3' Blog</title>", response.content)


