from seleniumrequests import Chrome
#
# webdriver = Chrome()
#
# count = 0
# url = 'http://192.168.77.130:8080/xss/reflect/post1'
# def ttt(driver,url,data):
#     '''
#     第一种方案：使用seleium来检测弹窗，优缺点：检测准确率高但效率低
#     :param str: payload
#     :return: alert or not
#     '''
#     isxss = False
#     response = driver.request(method='POST',url=url,data=data)
#     print(response)
#     try:
#         if driver.switch_to.alert:
#                 driver.switch_to.alert.accept()
#                 isxss = True
#     except Exception:
#         #driver.close()
#         pass
#     return isxss
#
# with open('XSSpayloads.txt') as f:
#     payload = f.readline().strip().split('=')
#     data = {}
#     data['in'] = payload[1]
#     if ttt(webdriver, url,data):
#         count += 1
# print(count)

from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('headless')  # 设置option
driver = webdriver.Chrome(chrome_options=option)
#webdriver.request('GET','http://192.168.77.130:8080/xss/reflect/post1')
#response = webdriver.request('POST', 'http://192.168.77.130:8080/xss/reflect/post1', data={"in": "\"><iframe/src=JavaScriPt:alert(45)>"})
from urllib.parse import urlencode
import time
request_url = 'http://192.168.77.130:8080/xss/reflect/post1'
data = {
    'p1': 'p1'
}
data_str = urlencode(data)
print(data_str)
ajax_query = """
        var xmlhttp=new XMLHttpRequest();
        xmlhttp.open(\"POST\",\"%s\",false);
        xmlhttp.setRequestHeader(\"Content-type\",\"application/x-www-form-urlencoded\");
        xmlhttp.send(\"%s\");
        return xmlhttp.responseText;
    """ % (request_url, data_str)
print(ajax_query)
t = int(round(time.time() * 1000))
resp = driver.execute_script(ajax_query)
print("take time(ms): ", int(round(time.time() * 1000)) - t)
print(resp)