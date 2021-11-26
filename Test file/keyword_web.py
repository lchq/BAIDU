# _*_coding:utf-8 _*-
# 测试：大锤
# @time: 18:46
# @file:keyword_web.py
from time import sleep

from selenium import webdriver

# 生成一个浏览器（webdriver对象）:反射机制
from selenium.webdriver.support.wait import WebDriverWait


def browser(type_):
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver

#定义工具类
class WebKeys:


    #构造函数
    def __init__(self,type_):
        self.driver = browser(type_)
        self.driver.implicitly_wait(10)


    #访问URL
    def open(self,**kwargs):
        self.driver.get(kwargs['txt'])

    #退出
    def quit(self,**kwargs):
        self.driver.quit()

    #元素定位
    def locator(self,**kwargs):
        return self.driver.find_element(kwargs['name'],kwargs['value'])


    #输入
    def input(self,**kwargs):
        self.locator(**kwargs).send_keys(kwargs['txt'])

    #点击
    def click(self,**kwargs):
        self.locator(**kwargs).click()


    #强制等待
    def wait(self,**kwargs):
        sleep(kwargs['txt'])

