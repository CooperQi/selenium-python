#coding=utf-8
from selenium import webdriver
import unittest
import public


class Login(unittest.TestCase):
    def setUp(self):
        public.setUp(self)

    def test_login(self):
        #u'''登录'''
        driver = self.driver
        public.login(self)
        self.assertEqual(driver.current_url, 'http://192.168.100.125:58088/vender/mainIndex.jsp')

        public.teardown(self)


if __name__ == '__main__':
    unittest.main()
