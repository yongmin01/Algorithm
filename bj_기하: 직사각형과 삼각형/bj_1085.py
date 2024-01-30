# 백준 기하: 직사각형과 삼각형_2 : 직사각형에서 탈출
[x, y, w, h] = [int(_) for _ in input().split()]
print(min(min(x, w-x), min(y, h-y)))