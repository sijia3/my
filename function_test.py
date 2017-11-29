from selenium import webdriver
import unittest


class test(unittest.TestCase):
    def setUp(self):
        self.brower = webdriver.Chrome()
    def tearDown(self):
        self.brower.quit()
    def test_can_start(self):
        self.brower.get('http://119.29.243.188')
        print self.brower.title
        self.assertIn("sijia3' Blog",self.brower.title)

if __name__ == '__main__':
    unittest.main()