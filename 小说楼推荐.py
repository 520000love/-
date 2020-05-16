
# 小说楼：https://www.xslou.com/
# 小说楼登录：https://www.xslou.com/login.php
# 小说楼的排行榜：https://www.xslou.com/top/allvisit_1/
# 小说楼推荐：https://www.xslou.com/modules/article/uservote.php?id=
import requests
from bs4 import BeautifulSoup


url_denglu = 'https://www.xslou.com/login.php'
url_paihangbang = 'https://www.xslou.com/top/allvisit_1/'
url_tuijian = 'https://www.xslou.com/modules/article/uservote.php?id='
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
data ={
'username': '账号',
'password': '密码',
'usecookie': '0',
'action': 'login',
'submit': '(unable to decode value)'}
cookies = 'PHPSESSID=4f1d321806b48f8f0badce62b8aba99e; jieqiUserInfo=jieqiUserId%3D151708%2CjieqiUserUname%3Dxx0487561oo%2CjieqiUserName%3Dxx0487561oo%2CjieqiUserGroup%3D3%2CjieqiUserGroupName%3D%C6%D5%CD%A8%BB%E1%D4%B1%2CjieqiUserVip%3D0%2CjieqiUserHonorId%3D%2CjieqiUserHonor%3D%D6%D0%BC%B6%BB%E1%D4%B1%2CjieqiUserPassword%3D0d045a7b88ce167a159e2e084460e5d1%2CjieqiUserUname_un%3Dxx0487561oo%2CjieqiUserName_un%3Dxx0487561oo%2CjieqiUserHonor_un%3D%26%23x4E2D%3B%26%23x7EA7%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserGroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%3D1588214883; jieqiVisitInfo=jieqiUserLogin%3D1588214883%2CjieqiUserId%3D151708; Hm_lvt_32da9a91d04e7f7f3eca588f6f08a0ae=1587884764,1588069140,1588166442,1588214892; Hm_lpvt_32da9a91d04e7f7f3eca588f6f08a0ae=1588214892'
cookies = {i.split('=')[0]:i.split('=')[1] for i in cookies.split(';')}
#请求登录
session = requests.session() 
session = session.post(url_denglu,headers = headers,cookies = cookies)
print(session.status_code)
#请求排行页和提取书名、编号
huo_id = requests.get(url_paihangbang)
print(huo_id.status_code)
huo_id.encoding = 'gbk'
jie_id = BeautifulSoup(huo_id.text,'html.parser')
ti_di = jie_id.find_all('span',class_="up2")
shu_zidian = {}
for i in ti_di:
    shu_shuming = i.find('a').text
    shu_lianjie = i.find('a')['href']
    shu_id_list = list(filter(str.isdigit,shu_lianjie))
    shu_id = ''.join(shu_id_list)
    shu_zidian[shu_id] = shu_shuming
    #print(shu_id)
#请求推荐
for a,b in shu_zidian.items():
    print(a,':',b)
shu_id = input('请输入要推荐书名的ID:')
url = url_tuijian+shu_id
#print(url)
re = requests.get(url,headers =headers,cookies=session.cookies)
re.encoding = 'gbk'
jie_jieguo =BeautifulSoup(re.text,'html.parser')
ti_jieguo = jie_jieguo.find(class_="blockcontent").text
print(ti_jieguo)


