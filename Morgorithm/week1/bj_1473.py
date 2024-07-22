# 백준 브루트포스 알고리즘 : 셀프 넘버

notSelfNum = []

for i in range(1, 10000) :
    s = str(i)
    num = 0
    for c in s :
        num += int(c)
    num += i
    notSelfNum.append(num)


for i in range(1, 10000) :
    if i not in notSelfNum :
        print(i)