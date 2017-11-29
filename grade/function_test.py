#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class visitor(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        pass
        # self.browser.quit()

    def test_can_login(self):
        self.browser.get('http://119.29.243.188/grade')
        # self.assertIn(u'网',self.browser.title)
        self.browser.find_element_by_id('inputText').send_keys('20150390109')
        self.browser.find_element_by_id('inputPassword').send_keys('5102110008')
        self.browser.find_element_by_id('login_100').send_keys(Keys.ENTER)



