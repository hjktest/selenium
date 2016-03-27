#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
#指定运行主机与端口号
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)
chromedriver="C:\Users\hjk\AppData\Local\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] =chromedriver
driver=webdriver.Chrome(chromedriver)
driver.get("http://www.youdao.com")
driver.find_element_by_name("q").send_keys("hello")
