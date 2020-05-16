import requests
import json

userid = str(888)
# 1 可以替换成任何长度小于32的字符串
apikey = str('钥匙')
# 这里的A，记得替换成你自己的apikey

# 创建post函数
def robot(neirong):
    # 图灵api
    api = r'http://openapi.tuling123.com/openapi/api/v2'
    # 创建post提交的数据
    data = {
        "perception": {
            "inputText": {              #输入文本
                "text": neirong
                         }
                      },
        "userInfo": {                   #用户信息
                    "apiKey": apikey,
                    "userId": userid,
                    }
    }
    # 转化为json格式
    jsondata = json.dumps(data)
    # 发起post请求
    huo = requests.post(api,data = jsondata)
    # 将返回的json数据解码
    huo = huo.content
    #转为二进制数据
    jie = json.loads(huo)
    # 提取对话数据
    ti = jie['results'][0]['values']['text']
    print(ti)

for x in range(5):
    neirong = input('talk:')
    # 输入对话内容 
    robot(neirong)
    print(x)

#当然咯，你也可以加一些stopwords，只要说了这些词就可以终止聊天
while True:
    neirong = input('talk:')
    # 输入对话内容 
    robot(neirong)
    if neirong == 'bye':
    # 设置stopwords
        break

# 创建对话死循环
while True:
    content = input('talk:')
    # 输入对话内容 
    robot(neirong)
