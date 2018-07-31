#coding=utf-8
from selenium import webdriver
import unittest
import public


class Login(unittest.TestCase):
    def setUp(self):
        public.setUp(self)

    def test_login(self):
        #u"""登录"""
        driver = self.driver
        driver.get(self.base_url)
        public.login(self)

    # def tearDown(self):
        public.teardown(self)


if __name__ == '__main__':
    unittest.main()
