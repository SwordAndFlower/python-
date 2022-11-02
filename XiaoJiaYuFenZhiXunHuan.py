#乘法表
a=1
while a<10:
	b = 9
	while b>=a:
		print(b,"*",a,"=",b*a,end="  ")
		b -= 1
	print()
	a +=1

print("-----"*20)

#素数
i=2
while i < 10:
    j=1
    counts = 0
    while j<=i:
        if i//j == i/j:
            counts += 1
        j += 1

    if counts <= 2:
        print(i,"是一个素数")
    else:
        j = 2
        while j < i :
            if i // j == i / j:

                print(i,"=",j,"*",i//j)
            j += 1
    i+=1



