from string import ascii_uppercase
aList = list(ascii_uppercase)
N, B = [int(x) for x in input().split()]
x = 0
while (N / B**x >= 1) :
    x += 1

x -= 1
result = []
while x >= 0 :
    result.append(N // B**x)
    N = N % B**x
    x -= 1

 
result2 = []

for x in result :
    if x > 10 :
        print(aList[x-10], end="")
    else :
        print(x, end="")