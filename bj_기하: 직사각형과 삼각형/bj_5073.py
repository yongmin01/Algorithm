# 백준 기하: 직사각형과 삼각형_7 : 삼각형과 세 변
while True :
    s = [a, b, c] = [int(x) for x in input().split()]
    if a == b == c == 0 :
        break
    else :
        if len(set(s)) == 1 :
            print("Equilateral")
        elif max(s) >= (sum(s)-max(s)) :
            print("Invalid")
        elif len(set(s)) == 3 :
            print("Scalene")
        else : print("Isosceles")