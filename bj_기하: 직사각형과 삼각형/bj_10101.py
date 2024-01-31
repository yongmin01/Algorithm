# 백준 기하: 직사각형과 삼각형_6 : 삼각형 외우기
d = []
for _ in range(3) :
    d.append(int(input()))
if sum(d) != 180 :
    print("Error")
elif d[0] == d[1] == d[2] == 60 : 
    print("Equilateral")
elif len(set(d)) == 3 :
    print("Scalene")
else : print("Isosceles")