chess = [1, 1, 2, 2, 2, 8]
n =[int(x) for x in input().split()]
result =[]
for x in range(6) :
        print(chess[x] - n[x], end=" ")
