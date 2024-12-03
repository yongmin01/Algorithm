N, M = [int(x) for x in input().split()]
basket = []
for x in range(N) :
    basket.append(x + 1)

for x in range(M): 
    i, j = [int(x) for x in input().split()]
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
for x in basket :
    print(x, end=" ")