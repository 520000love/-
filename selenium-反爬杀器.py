from selenium import webdriver  #从selenium库中调用webdriver模块
from bs4 import BeautifulSoup   #解析模块
import time #调用time模块计时
driver = webdriver.Chrome()     #设置引擎为Chrome
#请求登录页面
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
#登录第一个页面
ti = driver.find_element_by_id('teacher')
ti.send_keys('今天天气好')
time.sleep(2)
ti = driver.find_element_by_id('assistant')
ti.send_keys('明天天气更好')
time.sleep(2)
ti = driver.find_element_by_class_name('sub')
ti.click()
time.sleep(5)
#提取标题和正文
page_source = driver.page_source
jie = BeautifulSoup(page_source,'html.parser')
ti = jie.find_all(class_='content')
for i in ti:
    biaoti = i.find('h1').text
    zhengwen = i.find('p').text.replace('  ','')
    print(biaoti + '\n' +zhengwen +'\n')
#关闭浏览器
driver.close()




