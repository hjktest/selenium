#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import time
class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True
#百度搜索用例
    def test_baidu_search(self):
        u"""百度搜索"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()
    def test_baidu_login(self):
        u"""百度登录"""
        driver=self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_partial_link_text("登录").click()
        driver.find_element_by_id("TANGRAM__PSP_8__userName").clear()
        driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys("hjk03351")
        driver.find_element_by_id("TANGRAM__PSP_8__password").clear()
        driver.find_element_by_id("TANGRAM__PSP_8__password").send_keys("hjk123")
        driver.find_element_by_id("TANGRAM__PSP_8__submit").click()
        if driver.find_element_by_class_name("user-name").text=="hjk03351":
            print u"登录成功"
        else:
            print u"登录失败"

#百度设置用例
    def test_baidu_set(self):
        u"""百度设置"""
        driver = self.driver
#进入搜索设置页
        driver.get(self.base_url + "/gaoji/preferences.html")
#设置每页搜索结果为100 条
        m=driver.find_element_by_name("NR")
        m.find_element_by_xpath("//option[@value='50']").click()
        time.sleep(2)
 #保存设置的信息
        driver.find_element_by_xpath("/html/body/form/div/input").click()
        time.sleep(2)
        driver.switch_to_alert().accept()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__=="__main__":
    unittest.main()