#问答题
#0
#我以为一个是可变一个是不可变，所以False。但是结果是True
#1
#frozenset优势在于frozenset不可变，可以用它创建的集合来做字典的键
#2
#difference(*others)不改变原集合，而difference_update(*others) 会改变原集合
#3
#对
#4
#update(*others)是将*others中的每个元素逐个添加，而add(item)则是将item当成一个元素添加；
#*others可以是多个容器，而item只能是一个
#5
#remove(elem) 在删除elem元素时，如果没有这个元素，会报错，而当discard(elem) 删除elem元素时不会报错
#6
#去除FishCChsiF中的ish并乱序输出，且每个元素值留存一个





import hashlib as hb
import numpy as np
#动动手
#0
#利用 dict() 来实现交集和并集。
#题目要求：                               版权属于：https://fishc.com.cn
# 生成一个随机数列表，一共有 100 个元素，每个元素取 1~100 的随机值，赋值给变量 x
# 生成另一个随机数列表，一共有 100 个元素，每个元素取 50~150 的随机值，赋值给变量 y
# 利用字典的 “键” 不会重复的特点，计算 x 和 y 的交集（就是两者共有的元素）
list_x=[]
list_y=[]
for i in range(1,101):
    list_x.append(i)
for i in range(50,151):
    list_y.append(i)
x=np.random.choice(list_x,100,replace=True)
y=np.random.choice(list_y,100,replace=True)
#用来设置是否可以取相同元素：True表示可以取相同数字；False表示不可以取相同数字。默认是True
#字典的改动，会使得绑定的浅拷贝与字典的改动一起改变，所以用的字典都会从新生成

#并集
dict_all_u={}
for i in x:
    dict_all_u[i]=0
for i in y:
    dict_all_u[i]=0


#交集
dict_x_del_y={}
dict_y_del_x={}
for i in x:
    dict_x_del_y[i]=0
for i in y:
    dict_y_del_x[i]=0

for i in y:
    dict_x_del_y.pop(i,"")
for i in x:
    dict_y_del_x.pop(i,"")

dict_all_n={}
for i in x:
    dict_all_n[i]=0
for i in y:
    dict_all_n[i]=0

for i in dict_x_del_y:
    dict_all_n.pop(i,"")
for i in dict_y_del_x:
    dict_all_n.pop(i,"")

print("并集为：\n",list(dict_all_u.keys()),"\n","长度为：",len(dict_all_u),"\n",
      "交集为：\n",list(dict_all_n.keys()),"\n","长度为：",len(dict_all_n))


#1
# 题目要求：                                         Powered by https://fishc.com.cn
# 生成 0~999999 所有整数组成密码的哈希值
# 将上面生成的哈希值保存为映射类型
# 通过查表的方式，计算下面 3 个哈希值对应的明文密码
# 021bbc7ee20b71134d53e20206bd6feb
# e10adc3949ba59abbe56e057f20f883e
# 655d03ed12927aada3d5bd1f90f06eb7
#友情提示:
#hashlib.md5() 的参数是需要一个 b 字符串（即 bytes 类型的对象），
# 这里可以使用 bytes("123", "utf-8") 的方式将 "123" 转换为 b"123"。
dict_hash={}
for i in range(1,1000000):
    dict_hash[i]=hb.md5(bytes(str(i), "utf-8")).hexdigest()
# 生成 0~999999 所有整数组成密码的哈希值,将上面生成的哈希值保存为映射类型
#注：所有数值相等的哈希值都是一样的，即hash(0)==hash(000000)
code1="021bbc7ee20b71134d53e20206bd6feb"
code2="e10adc3949ba59abbe56e057f20f883e"
code3="655d03ed12927aada3d5bd1f90f06eb7"
index1=0
index2=0
index3=0
for i in list(dict_hash.values()):
    if code1==str(i):
        index1=list(dict_hash.values()).index(i)
    if code2==str(i):
        index2=list(dict_hash.values()).index(i)
    if code3==str(i):
        index3=list(dict_hash.values()).index(i)
decode1=list(dict_hash.keys())[index1]
decode2=list(dict_hash.keys())[index2]
decode3=list(dict_hash.keys())[index3]
print(code1,"\n的破译密码是：",decode1,"\n",
      code2,"\n的破译密码是：",decode2,"\n",
      code3,"\n的破译密码是：",decode3,"\n",)
#这里尝试多次，始终没有明白为什么if没有执行。我放弃了，来看小甲鱼的方案
#上述已经将问题解决，出在bytes("123", "utf-8")这里，原来用的是b"i"，具体这些差别，还不懂，等以后学到再说


# rainbow_table = {}
#
# for i in range(1000000):
#     bstr = bytes(str(i), "utf-8")
#     s = hashlib.md5(bstr).hexdigest()
#     rainbow_table[s] = i
#
# s1 = "021bbc7ee20b71134d53e20206bd6feb"
# s2 = "e10adc3949ba59abbe56e057f20f883e"
# s3 = "655d03ed12927aada3d5bd1f90f06eb7"
#
# print(f"{s1} 对应的明文是：{rainbow_table[s1]}")
# print(f"{s2} 对应的明文是：{rainbow_table[s2]}")
# print(f"{s3} 对应的明文是：{rainbow_table[s3]}")



