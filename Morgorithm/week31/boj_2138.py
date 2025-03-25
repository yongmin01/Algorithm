# 백준_그리디 알고리즘 : 전구와 스위치

import sys
import copy
input = sys.stdin.readline

N = int(input())
prev = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))

# 목표 상태가 초기와 같은 경우
if prev == target :
    print(0)
    exit()
    
def solution(arr, cnt) :
    for i in range(1, N) : 
        if arr[i-1] != target[i-1] :
            cnt += 1
            arr[i -1] = int(not arr[i-1])
            arr[i] = int(not arr[i])
            if i < N-1 :
                arr[i+1] = int(not arr[i+1])
    if arr == target :
        return cnt
    else : return False

answer = []
current = copy.deepcopy(prev)

# 첫 번째 전구를 켜지 않는 경우
skip_first_bulb = solution(current, 0)
if skip_first_bulb :
    answer.append(skip_first_bulb)
else :
    # 첫 번째 전구를 켜는 경우
    current = copy.deepcopy(prev)
    current[0] = int(not current[0])
    current[1] = int(not current[1])
    push_first_bulb = solution(current, 1)
    if push_first_bulb :
        answer.append(push_first_bulb)
if len(answer) > 0 :
    print(min(answer))
else :
    print(-1)

