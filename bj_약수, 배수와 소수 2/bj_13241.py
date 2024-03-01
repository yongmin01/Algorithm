# 백준 약수, 배수와 소수 2_2 : 최소공배수
import sys

[A, B] = list(map(int, sys.stdin.readline().split()))
if A >= B :
    MAX = A
    MIN = B
else :
    MAX = B
    MIN = A
temp = MAX
count = 1
while temp % MIN != 0 :
    temp += MAX
    count += 1
print(MAX*count)