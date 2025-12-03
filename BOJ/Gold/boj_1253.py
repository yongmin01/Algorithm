# [백준] 투포인터 > 좋다

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
answer = 0
for i in range(n) :
    s, e = 0, n-1
    while 0 <= s < e < n :
        if s == i : s += 1
        if e == i : e -= 1
        if s < e :
            if nums[s] + nums[e] == nums[i] : 
                answer += 1
                break

            elif nums[s] + nums[e] < nums[i] : s += 1
            else : e -= 1
        else : break
print(answer)