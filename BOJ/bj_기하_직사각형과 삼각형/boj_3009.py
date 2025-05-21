# 백준 기하: 직사각형과 삼각형_3 : 네 번째 점
X = []
Y = []
for _ in range(3) :
    [x, y] = [int(_) for _ in input().split()]
    X.append(x)
    Y.append(y)

if X[0] == X[1] :
    X = X[2]
elif X[0] == X[2] : 
    X = X[1]
else :
    X = X[0]

if Y[0] == Y[1] :
    Y = Y[2]
elif Y[0] == Y[2] : 
    Y = Y[1]
else :
    Y = Y[0]

print(X, Y)