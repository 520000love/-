#调用库
import requests     
from bs4 import  BeautifulSoup      
#获取-请求
huo = requests.get('http://books.toscrape.com/')
#获取-打印-响应码
print(huo.status_code)
#获取-返回值类型
fan = huo.text
#解析-解析返回值，实例化
jie = BeautifulSoup(fan,'html.parser')
#提取-定位-定位解析的数据
ti = jie.find_all(class_="product_pod")
#提取-遍历（消除列表，定位具体数据）
for i in ti:
    kind = i.find('h3').find('a')
    lind = i.find('p',class_="star-rating")
    nind = i.find('div',class_="product_price").find('p',class_="price_color")
  #  print(lind)
#提取-打印数据    
    print(kind['title'])    #提取'title'的值
    print('star-rating:',lind['class'][1])  #lind['class']取出class的值，[1]取出序号1的值
    print('Price:',nind.text, end='\n'+'------'+'\n')   #加换行符，美观