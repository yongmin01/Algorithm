# [백준] 이분 탐색 > 나무 자르기

n, m = map(int, input().split(" "))
trees = list(map(int, input().split(" ")))
start, mid, end = 0, max(trees) // 2, max(trees)
answer = 0
while start <= end :
    acc = 0
    for tree in trees :
        if tree > mid : acc += tree - mid
    if acc >= m : 
        answer = max(answer, mid)
        start = mid + 1
        mid = (start + end) // 2
    else :
        end = mid - 1
        mid = (start + end) // 2

print(answer)