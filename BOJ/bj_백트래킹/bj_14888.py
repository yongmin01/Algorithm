# 백준 백트래킹_7 : 연산자 끼워넣기
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

min_val = 1e9
max_val = -1e9

def operate(depth, n, result, add, minus, multiply, divide) : 
    global min_val, max_val
    if depth == n-1 :
        min_val = min(result, min_val)
        max_val = max(result, max_val)
        return
    
    if add > 0 :
        operate(depth + 1, n, result + nums[depth+1], add - 1, minus, multiply, divide)
    if minus > 0 :
        operate(depth + 1, n, result - nums[depth+1], add, minus - 1, multiply, divide)
    if multiply > 0 :
        operate(depth + 1, n, result * nums[depth+1], add, minus, multiply - 1, divide)
    if divide > 0 :
        if result > 0 :
            operate(depth + 1, n, result // nums[depth+1], add, minus, multiply, divide - 1)
        else :
            operate(depth + 1, n, -(result // -nums[depth+1]), add, minus, multiply, divide - 1)

operate(0, N, nums[0], operators[0], operators[1], operators[2], operators[3])
print(max_val)
print(min_val)