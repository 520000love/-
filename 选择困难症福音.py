import random 
a = ['粤菜','鲁菜','川菜','苏菜','浙菜','闽菜','湘菜','徽菜']
for i in range(10):
    xuanzhong = random.choice(a)
    xuanze = input ('%s,任意键继续推荐，满意按n退出'%xuanzhong)
    print(xuanze)
    if xuanze == 'n':
        break
print('你今天不用吃饭了')




