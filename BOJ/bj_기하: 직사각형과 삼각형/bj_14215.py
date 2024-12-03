# 백준 기하: 직사각형과 삼각형_8 : 세 막대
s = [a, b, c] = [int(x) for x in input().split()]
if max(s) >= sum(s) - max(s) :
    print(2*(sum(s) - max(s)) -1)
else : print(sum(s))