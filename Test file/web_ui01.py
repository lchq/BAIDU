# _*_coding:utf-8 _*-
# 测试：大锤
# @time: 22:09
# @file:web_ui01.py
'''
1，访问一条热搜
2，百度搜一下
'''
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(10)
#访问第一条热搜
driver.find_element('xpath','//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]').click()
sleep(3)
#切换页面，获取浏览器句柄
handles=driver.window_handles
#切换句柄到第1个页面
driver.switch_to.window(handles[0])
sleep(2)
#百度一下搜索
driver.find_element('id','kw').send_keys(123)
driver.find_element('id','su').click()
sleep(2)
driver.quit()


