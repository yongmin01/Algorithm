# 백준 정렬_2 : 대표값2

arr = []
for i in range(5) :
    arr.append(int(input()))
print(sum(arr)//5)
print(sorted(arr)[2])
