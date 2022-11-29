#问答题
#0
#0 8 5 2 1
#1
#[70, 105, 115, 104, 67]
#2
#list(map(sorted,matrix))
#3
#报错
#4
#a=[i for i in "FishC" if i.islower()]
#5
# x = [1, 2, 3, 4, 5]
# y = "FishC"
# z=zip(x,y)
# for i in z:
# 	print(i)
#6
#迭代器是一次性的，而可迭代对象可以重复使用
#7
#可以



#动动手
#0
#请使用学过的知识，自己动手编写代码，利用 for 循环语句，模拟 all()、any()、enumerate()、zip() 这4个函数的实现。
#all（）判断可迭代对象中所有元素的值是否为真
# x=[]
# x=input("shurushuzi")
# count=0
# for i in x:
#     if int(i) != 0:
#         count=count+1
#     else:
#         count=0
# if count==len(x):
#     print("True")
# else:
#     print("False")

# #any（）则是判断可迭代对象中是否存在某个元素的值为真
# x=[]
# x=input("输入数字")
# count=0
# for i in x:
#     if int(i) != 0:
#         count=1
#         break
# if count==1:
#     print("True")
# else:
#     print("False")

# #enumerate（）函数用于返回一个枚举对象，将迭代对象中的每个元素及从0开始的序号共同构成一个二元组的列表
# x=["asjhd","asghdfsgah","gasgh"]
# z=()
# b=[]
# y=input("输入开始的数字")
# count=int(y)
# for i in x:
#     z=(count,i)      ##enumerate是返回枚举类型，打印的时候是几个元组打印出来，元组有两个元素，前面的是数字，后面的字符串
#     b.append(z)
#     count=count+1
# print(b)

#zip()函数用于创建一个聚合多个可迭代对象的迭代器，它会将作为参数传入的每个可迭代对象的每个元素依次组合成元组，即第i个元组包含来自每个参数的第i个元素
x=[1,2,3,4]
y=[7,8,9,0,9]
z=[]
a=()
b=0
c=0
if len(x)>len(y):
    c=len(x)
else:
    c=len(y)
for i in range(c):
    a=(x[b],y[b])
    z.append(a)
    b=b+1
print(z)
