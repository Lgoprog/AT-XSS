#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 11:03 PM
# @Author  : w8ay
# @File    : plugins.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoAlertPresentException

import time
firstTime = True
def selenium_xss(driver,url):
    '''
    第一种方案：使用seleium来检测弹窗，优缺点：检测准确率高但效率低
    :param str: payload
    :return: alert or not
    '''
    global firstTime
    if not firstTime:
        driver.execute_script("window.open();")
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(url)
    else:
        driver.get(url)
        firstTime = False
    isxss = False
    try:
        # 尝试切换到alert
        alert = driver.switch_to.alert
        alert.accept()
        isxss = True
    except NoAlertPresentException:
        # 没有alert时不执行任何操作
        pass

    return isxss

def check_xss(url):

    # 第一种方案：使用seleium来检测弹窗，优缺点：检测准确率高但效率低
    # :param str: payload
    # :return: alert or not
    option = Options()
    #option.add_argument('headless')  # 设置option
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    isxss = False
    try:
        # 尝试切换到alert
        alert = driver.switch_to.alert
        alert.accept()
        isxss = True
    except NoAlertPresentException:
        # 没有alert时不执行任何操作
        pass
    driver.close()
    return isxss

# def check_xss(driver,url):
#
#     # 第一种方案：使用seleium来检测弹窗，优缺点：检测准确率高但效率低
#     # :param str: payload
#     # :return: alert or not
#     driver.get(url)
#     isxss = False
#     if driver.switch_to.alert:
#         driver.switch_to.alert.accept()
#         isxss = True
#     driver.close()
#     return isxss

def init_webdriver():
    option = Options()
    #option.add_argument('headless')  # 设置option
    global driver
    driver = webdriver.Chrome(options=option)
    return driver

if __name__ == '__main__':
    ##读取payload集合并验证是否存在弹窗
    s = time.time()
    driver = init_webdriver()
    count = 0
    with open('XSSpayloads.txt') as f:
        while True:
            url = f.readline().strip()
            if not url:
                break
            if selenium_xss(driver,url):
                count +=1
                print(count)
            e = time.time()
            print('Cost Time', e - s)



