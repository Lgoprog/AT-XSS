from lib.gym.envs.helper import selenium_xss,init_webdriver

driver = init_webdriver()
# 我们先打开一个网页
if selenium_xss(driver,"https://www.zhipin.com/user/login.html"):
    print(1)
# 浏览器 新窗口打开连接
newwindow = 'https://www.baidu.com'
if selenium_xss(driver,newwindow):
    print(1)
if selenium_xss(driver,newwindow):
    print(1)
if selenium_xss(driver,newwindow):
    print(1)
# driver.execute_script(newwindow)
# # 移动句柄，对新打开页面进行操作
# driver.switch_to.window(driver.window_handles[0])
# # 具体操作
# driver.find_element_by_xpath("")
# # 关闭该新打开的页面
# driver.close()
# # 不关闭，要移动到上一个页面，我们要移动句柄
# driver.switch_to.window(driver.window_handles[0])