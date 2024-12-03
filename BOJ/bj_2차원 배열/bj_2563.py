n = int(input())
square = [[0]*100 for _ in range(100)]
result = 0

for _ in range(n) :
    x,y = [int(l)-1 for l in input().split()]

    for m in range(x, x+10) :
        for n in range(y, y+10) :
            if square[m][n] != 1 :
                square[m][n] = 1

for _ in range(100) :
    result = result + square[_].count(1)
print(result)

