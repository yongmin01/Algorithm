N, M = [int(x) for x in input().split()]
basket = []
for x in range(N) :
    basket.append(x+1)

for x in range(M) :
    i, j = [int(x) for x in input().split()]
    temp = []
    for y in range(i-1, j) :
        temp.append(basket[y])
    times = len(temp)-1
    for z in range(i-1, j) :
        basket[z] = temp[times]
        times -= 1
    
for x in basket :
    print(x, end=" ")
