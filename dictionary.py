#问答题
#0
# 可以
#1
#{'小甲鱼': '千年王八，万年龟。'}
#2
#{'小甲鱼': {'数学': 99, '英语': 88, '语文': 100}}
# 我以为可以，试了之后不可以。区别难道是因为字典的嵌套？
#答：切片和拷贝都是浅拷贝，浅拷贝只拷贝外层的对象，如果包含嵌套的话，拷贝的只是其引用。
#3
#{1: '万年龟'}
#我以为应该是{1: '千年王八'，1.0: '万年龟'}
#原因：值相等的数字表示相同的键，即整型数字1和浮点数1.0的哈希值是相同的，它们是相同的键。
#4
#随着字典的改变，他们也改变
#5
#get(,)
#6
#字典的推导式，会将最左边的for运行一次的结果给到前面，而最左边的for运行一次会使得后面的运行完，所以后面的for每次都得到6，将值传给上层


import hashlib as hb
#动动手
#0
# 请按照要求编写一个网站的注册模块                   来自：https://fishc.com.cn
# 我们知道，通常一个网站的用户名都是唯一的，这就要求注册的时候，系统代码可以识别当前输入的用户名是否已经存在？
# 如果存在，则不允许注册！                         来自：https://fishc.com.cn
# 那么现在请大家一起来动手，编写一个网站的注册模块。
# 要求：                                       版权属于：https://fishc.com.cn
# 用户名不允许重复
# 数据库需要保存用户名及密码
# 初始用户及密码（"小甲鱼":"I_love_FishC"，"不二如是":"FishC5201314"）
username_password={"小甲鱼":"I_love_FishC","不二如是":"FishC5201314"}
print("请输入用户名：")
while(1):
    username=input()
    exist=username_password.get(username,"没")
    if exist=="没":
        print("请输入密码：")
        password=input()
        username_password[username]=password
        break
    else:
        print("该用户名已被注册！")
        print("请重新输入用户名：")

print("--"*30)
print("目前已注册的用户有：")
username_all=username_password.keys()
password_all=username_password.values()
for i in range(len(username_all)):
    print(list(username_all)[i],":",
          # 1#密码明文加密
          hb.md5(b"list(password_all)[i]").hexdigest()
          #这里的b一定要有，具体用法尚不清楚，但应该和格式化字符串f一样
          )


