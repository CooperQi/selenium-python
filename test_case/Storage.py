# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import public

class Storage(unittest.TestCase):
    def setUp(self):
        public.setUp(self)
    
    def test_storage(self):
        driver = self.driver
        public.login(self)

        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='常用操作'])[1]/following::a[1]").click()
        driver.switch_to.frame(u"产品入库")
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='经销商名称：'])[1]/preceding::a[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='客户类型'])[1]/following::span[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='显示1到11,共11记录'])[1]/following::a[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='单据备注：'])[1]/following::span[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='产品型号:'])[2]/following::a[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='C4'])[3]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='显示1到20,共200106记录'])[1]/following::a[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='产品数量:'])[1]/following::input[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='产品数量:'])[1]/following::input[2]").clear()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='产品数量:'])[1]/following::input[2]").send_keys("1")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='销售单位:'])[1]/following::a[1]").click()
        driver.find_element_by_id("_easyui_combobox_i23_0").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='厂商代码：'])[1]/following::span[3]").click()
    
    def is_element_present(self, how, what,timeout=10):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
