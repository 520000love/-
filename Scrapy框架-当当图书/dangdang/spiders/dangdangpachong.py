import scrapy
import bs4
from ..items import DangdangItem

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'   #爬虫名
    allowed_domains = ['http://bang.dangdang.com']  #过滤域名
    start_urls = [] #起始网页
    #起始网页制作
    for x in range(1, 4):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-' + str(x)
        start_urls.append(url)

    #响应解析提取
    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'html.parser')  #解析
        elements = soup.find('ul', class_="bang_list clearfix bang_list_mode").find_all('li')   #最小父级标签
        for element in elements:    #提取目标数据
            item = DangdangItem()
            item['name'] = element.find('div', class_="name").find('a')['title']
            item['author'] = element.find('div', class_="publisher_info").text
            item['price'] = element.find('div', class_="price").find('span', class_="price_n").text
            yield item  #数据传送至引擎