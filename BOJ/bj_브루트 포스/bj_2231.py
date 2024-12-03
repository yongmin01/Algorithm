# 백준 브루트 포스_2 : 분해합

N = int(input())

for i in range(N) :
    j = []
    for l in range(len(str(i))):
        j.append(str(i)[l])
    s = 0
    for m in j :
        s += int(m)
    if s + i  == N :
        print(i)
        break
    if i == N - 1 :
        print(0)