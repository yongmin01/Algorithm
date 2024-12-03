N, M = [int(x) for x in input().split()]
basket = [0 for x in range(N)]
for x in range(M): 
    i, j, k = [int(x) for x in input().split()]
    for y in range(i - 1, j) :
        basket[y] = k
for x in basket :
    print(x, end=" ")