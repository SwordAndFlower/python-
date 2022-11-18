import os
import numpy as np
#问答题
#0  在3.7.4之前并不适用
#1  {1+2}
#2  {3}
#3  f"{3.1415:.2f}"
#4  报错
#5  f"{3.14:{fill}{align}{width}.{prec}{ty}}"


#动动手
#0  利用字符重复出现的次数，编写一个程序，实现基本的字符串压缩功能。
#       比如，字符串 FFiiiisshCCCCCC 压缩后变成 F2i4s2h1C6（15字符 -> 10字符，66% 压缩率）。
#       这种朴素的压缩算法并不总是理想的，比如 FFishCC 压缩后反而变长了 F2i1s1h1C2，这可就不是我们想要的了，
#       所以对于重复次数小于 3 的字符，我们的程序应该选择不对其进行压缩。
#   预计实现效果
#       请输入待压缩字符串：FFiiiisshCCCCCC
#       压缩后的字符串：FFi4sshC6
#       压缩率为：60.00%
str_pack=input("请输入待压缩字符串：")
a=[]
for i in range(len(str_pack)):
    if str_pack.count(str_pack[i],i,i+3)<3:
        if str_pack[i-2]==str_pack[i]:
            continue
        if str_pack[i-1]==str_pack[i+1]:
            continue
        a.append(str_pack[i])
    elif str_pack.count(str_pack[i],i,i+3)>=3:
        for j in range(len(str_pack)-i-2):
            if str_pack[i]==str_pack[i+2+j]:
                count = 3+j
        if str_pack[i-1]==str_pack[i]:
            continue
        a.append(str_pack[i])
        a.append(str(count))
c = ''.join(a)
print("压缩后的字符串：",c)
b=len(a)/len(str_pack)
print("压缩率为：",f"{b:.2f}")

#1  请大家编写一个解压程序，将上一题压缩后的字符串进行解压缩。
#   预计实现效果
#       请输入待解压字符：FFi4sshC6
#       解压后的字符串：FFiiiisshCCCCCC
str_unpack=input("请输入待解压字符：")
x=np.fromstring(str_unpack,dtype=np.uint8)
y=[]
for i in range(len(str_unpack)):
    if i<len(str_unpack)-1:
        if 50<x[i+1] and x[i+1]<58:
            y.append(str_unpack[i]*int(chr(x[i+1])))
    if 50<x[i]<58:
        continue
    y.append(str_unpack[i])
z=''.join(y)
print("解压后的字符串：",z)



