#coding=utf-8
from selenium import webdriver
import unittest,time

import csv

#def readUser():
my_file = 'D:/selenium_python/data/userinfo.csv'
data = csv.reader(file(my_file, 'rb'))
for user in data:
    us = user[0]
    pw = user[1]



def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(30)
    self.base_url = "http://222.191.229.126:58088/vender/index.jsp"
    self.verificationErrors = []
    self.accept_next_alert = True

def login(self):
    driver = self.driver
    username = driver.find_element_by_id("account_num")
    username.clear()

    username.send_keys(us.decode("utf-8"))
    #username.send_keys("admin")
    passwd = driver.find_element_by_id("mima")
    passwd.clear()
    passwd.send_keys(pw.decode("utf-8"))
    #passwd.send_keys("QSqwe#@!")
    driver.find_element_by_id("focusub").click()

def teardown(self):
    self.driver.close()