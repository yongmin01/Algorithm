# 백준_비트마스킹 : 막대

X = int(input())

arr = [0, 0, 0, 0, 0, 0, 1]
amount = [0, 0, 0, 0, 0, 0, 1]

def stickSum() :
    sum = 0
    for a in range(7) :
        if amount[a] >= 1 :
            sum += (2 ** a) * amount[a]
    return sum

while stickSum() > X :
    shortestIndex = arr.index(1)
    shortest = 2 ** shortestIndex
    amount[shortestIndex] -= 1
    if amount[shortestIndex] == 0 : arr[shortestIndex] = 0
    amount[shortestIndex-1] += 2
    arr[shortestIndex-1] = 1
    if stickSum() - (shortest / 2) >= X :
        amount[shortestIndex-1] -= 1
    
    if stickSum() == X :
        break
    else : continue

print(sum(amount))

