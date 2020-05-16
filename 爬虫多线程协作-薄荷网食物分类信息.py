from gevent import monkey
monkey.patch_all()
import gevent,requests, bs4, csv
from gevent.queue import Queue

work = Queue()

#前3个常见食物分类的前3页的食物记录的网址：
url_1 = 'http://www.boohee.com/food/group/{type}?page={page}'
for x in range(1, 4):
    for y in range(1, 4):
        real_url = url_1.format(type=x, page=y)
        work.put_nowait(real_url)
      
#第11个常见食物分类的前3页的食物记录的网址：
url_2 = 'http://www.boohee.com/food/view_menu?page={page}'
for x in range(1,4):
    real_url = url_2.format(page=x)
    work.put_nowait(real_url)

#请写出crawler函数和启动协程的代码：
def dongzuo():
    while not work.empty():
        url = work.get_nowait()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        huo = requests.get(url,headers)
        #print(huo.status_code)
        jie = bs4.BeautifulSoup(huo.text,'html.parser')
        ti = jie.find_all('li',class_="item clearfix")
        for i in ti:
            mingzi = i.find_all('a')[1]['title']
            lianjie = 'http://www.boohee.com' + i.find_all('a')[1]['href']
            erliang = i.find('p').text
            writer.writerow([mingzi,erliang,lianjie])
csv_cun = open('各种食物热量.csv','w',newline='',encoding = 'utf-8')
writer = csv.writer(csv_cun)
writer.writerow(['食物','热量','链接'])

renwu_xiezuo = []
for i in range(2):
    xiezuo = gevent.spawn(dongzuo)
    renwu_xiezuo.append(xiezuo)

gevent.joinall(renwu_xiezuo)
csv_cun.close()
print('胜利')

