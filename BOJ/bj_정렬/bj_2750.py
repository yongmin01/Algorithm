# 백준 정렬_1 : 수 정렬하기
N = int(input())
arr = []
for i in range(N) :
    arr.append(int(input()))

arr.sort()
for i in range(N) :
    print(arr[i])
