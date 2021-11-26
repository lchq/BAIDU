# _*_coding:utf-8 _*-
# 测试：大锤
# @time: 18:48
# @file:web_ui.py


'''
百度登录
'''

from demo1.keyword_web import WebKeys
import openpyxl
# 访问excel内容，生成工作簿
excel = openpyxl.load_workbook(r'C:\Users\DELL\PycharmProjects\BAIDU\demo2\shuju\canshu.xlsx')
sheet = excel['Sheet1']
# 读取excel内容，实现文件驱动自动化执行
for value in sheet.values:
    # 定义一个字典参数，用于接收excel中的所有参数内容
    args = {}
    args['name'] = value[2]
    args['value'] = value[3]
    args['txt'] = value[4]

    # 基于A列进行判断是否为测试用例
    if type(value[0]) is int:
        # 判断是否实例化
        if value[1] == 'open_browser':
            wk = WebKeys(value[4])
        # 非特殊关键字，通过反射机制实现
        else:
            getattr(wk, value[1])(**args)

