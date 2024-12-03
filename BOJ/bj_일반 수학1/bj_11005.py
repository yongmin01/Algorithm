from string import ascii_uppercase
aList = list(ascii_uppercase)
N, B = [int(x) for x in input().split()]
result = ''
while N != 0 :
    if (N % B < 10) :
        result = str(N%B) + result
    else :
        result = aList[N%B-10] + result
    N = N // B
print(result)