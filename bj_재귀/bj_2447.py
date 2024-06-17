# 백준 재귀_6 : 별 찍기 - 10 
def star(n):
    if n == 1:
        return ["*"]
    result = []
    for i in star(n//3):
        result.append(i*3)
    for i in star(n//3):
        result.append(i + " "* (n//3) + i)
    for i in star(n//3):
        result.append(i*3)
    return result

N = int(input())
print("\n".join(star(N)))