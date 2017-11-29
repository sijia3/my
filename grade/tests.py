# -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from blog.models import BlogsPost
from grade.views import *
from django.test import Client
from selenium import webdriver
import django.utils.timezone as timezone

class Test(TestCase):
    # def test_url(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func,index)
    # def test_index_returns_current_html(self):
    #     request = HttpRequest()
    #     response = index(request)
    #     print response
    #     self.assertIn(b"<title>sijia3ww' Blog</title>", response.content)
    #     respone = self.client.get('/user/imformation/')
    #     print respone
    #     self.assertIn(b"大佬，你", respone.content)
    #
    #     response = self.client.post('/', {'username' : "12", 'password' : "12"})
    #     print response
        def test_can_login(self):
            # request = HttpRequest()
            # request.method = 'POST'
            # request.POST['user'] = '20150390109'
            # request.POST['pw'] = '5102110008'
            # response = login_user(request)
            # self.assertEqual(response.status_code,302)
            response = self.client.post('/grade/', data={'user': '20150390109', 'pw': '5102110008'})
            response = self.client.get(response.url)
            # print response



