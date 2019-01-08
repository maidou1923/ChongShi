#coding:utf-8
from selenium import webdriver

# browser = webdriver.Firefox #这里使用Firefox，用其它浏览器的话需要安装浏览器驱动
browser = webdriver.Chrome
browser.get("http://www.baidu.com")

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()

browser.quit()

