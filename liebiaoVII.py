#问答题
#0
#临时的，没什么意义
#1
# a = [[8 for i in range(4)]  for j in range(5)]
# print(a)
#2
# result = []
# for i in range(10):
#     if i%2 == 0:
#         result.append(i/2)
#         i = i+1
# print(result)
#3
# result = [[x,y] for x in range(10) if x%2 == 0 for y in range(10) if y%2 != 0]
# print(result)
#4
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# fanzhuan = [10-x for y in matrix for x in y]
# print(fanzhuan)
#5
# colors = ["BLACK", "WHITE"]
# sizes = ["WS", "WM", "WL", "S", "M", "L", "XL", "2XL", "3XL", "4XL"]
# result = [[x,y] for x in colors for y in sizes]
# print(result)
#动动手
#0
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12]]
# Tmatrix = [[x[i] for x in matrix] for i in range(4)]
# ##x取的是matrix的每一行，然后，x[i]取的是每一行的第i个元素，使得[x[i] for x in matrix]是一个一行三列，依次再取3
# print(Tmatrix)
#1
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
#(0,0)->(0,1)->(0,2)->(0,3)->(1,3)->(2,3)->(2,2)->(2,1)->(2,0)->(1,0)->(1,1)->(1,2)
kong=[]
for i in range(4):
    kong.append(matrix[0][i])
for j in range(2):
    kong.append(matrix[j+1][3])
for x in range(3):
    kong.append(matrix[2][2-x])
for y in range(3):
    kong.append(matrix[1][y])
print(kong)