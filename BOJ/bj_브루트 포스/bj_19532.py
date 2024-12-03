# 백준 브루트 포스_3 : 수학은 비대면강의입니다

# 무지성 답안
# [a, b, c, d, e, f] = [int(x) for x in input().split()]
# if a == 0 :
#     y = c //b
#     x = (f - e*y) // d
# elif b == 0 :
#     x = c // a
#     y = (f - d*x) // e
# elif d == 0 :
#     y = f // e
#     x = (c - b*y) // a
# elif e == 0 :
#     x = f // d
#     y = (c - a*x) // b
# else :
#     y = (a*f-c*d) // (a*e - b*d)
#     x = (c - b*y) // a
# print(x, y)

# 브루트 포스 알고리즘 적용
[a, b, c, d, e, f] = [int(x) for x in input().split()]
def cal (a, b, c, d, e, f) :
    for x in range(-999, 1000) :
        for y in range(-999, 1000) :
            if (a*x + b*y == c and d*x + e*y == f) :
                print(x, y)
                
cal (a, b, c, d, e, f)