# 백준 기하: 직사각형과 삼각형_5 : 대지
N = int(input())
X = []
Y = []
for _ in range(N) :
    [x, y] = [int(n) for n in input().split()]
    X.append(x)
    Y.append(y)
X = set(X)
Y = set(Y)

if (len(X) == 0 or len(Y) == 0) :
    print(0)
else :
    print((max(X) - min(X))* (max(Y) - min(Y)))