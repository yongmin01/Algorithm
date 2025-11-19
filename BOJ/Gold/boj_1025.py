# [백준] 브루트포스 > 제곱수 찾기

import sys, math
input = sys.stdin.readline
n, m = map(int, input().split(" "))

nums = []
for _ in range(n) :
    nums.append(input().strip())

answer = -1
# 모든 점이 시작점이 될 수 있도록 순회
for r in range(n) :
    for c in range(m) :
        num = nums[r][c]
        temp = int(math.sqrt(int(num)))
        if temp * temp == int(num) :
            answer = max(answer, int(num))
        # 가능한 모든 공차의 조합(rd : 행의 공차, cd : 열의 공차)
        for rd in range(-(n-1), n) :
            for cd in range(-(m-1), m) :
                nr = r + rd
                nc = c + cd
                if 0 <= nr < n and 0 <= nc < m :
                    # 행과 열의 공차가 모두 0인 경우는 시작점을 지정할 때 고려했으므로 pass
                    if rd == 0 and cd == 0 :
                        continue
                    # 현재 공차 조합으로 지정된 점이 matrix 안에 속하는 경우에는 선택하여 수를 이어붙임
                    while 0 <= nr < n and 0 <= nc < m :
                        num += nums[nr][nc]
                        temp = int(math.sqrt(int(num)))
                        if temp * temp == int(num) :
                            answer = max(answer, int(num))
                        nr += rd
                        nc += cd
                num = num[0] # 공차가 바뀌면 시작점만 남기고 초기화
                
print(answer)