
# [백준] 백트래킹 > 색종이 붙이기

import sys
input = sys.stdin.readline

arr = []
for r in range(10) :
    arr.append(list(map(int, input().split())))

answer = 25
papers = [0, 5, 5, 5, 5, 5]
def find_one() :
    for r in range(10) :
        for c in range(10) :
            if arr[r][c] == 1 :
                return [r, c]
    return [-1, -1]

def can_attach(size, x, y) :
    if x+size <= 10 and y+size <= 10 :
        for c in range(y, y+size) :
            if arr[x][c] != 1 : return False
        for r in range(x+1, x+size) :
            if arr[r][y:y+size] != arr[x][y:y+size] : return False
        return True
    else : return False

def attach(size, x, y) :
    for r in range(x, x+size) :
        for c in range(y, y+size) :
            arr[r][c] = 0

def detach(size, x, y) :
    for r in range(x, x+size) :
        for c in range(y, y+size) :
            arr[r][c] = 1

def dfs(cnt) :
    global answer
    if cnt >= answer : return
    x, y = find_one()
    if x == -1 : 
        answer = min(answer, cnt)
        return

    for size in range(5, 0, -1) :
        if papers[size] == 0 :
            continue
        if can_attach(size, x, y) :
            attach(size, x, y)
            papers[size] -= 1
            dfs(cnt+1) 
            detach(size, x, y)
            papers[size] += 1

dfs(0)
print(answer if answer != 25 else -1)


# 그리디로 풀기 실패!

# import heapq

# arr = []
# spots = []
# for r in range(10) :
#     row = list(map(int, input().split()))
#     for c in range(10) :
#         if row[c] == 1 : spots.append([r, c])
#     arr.append(row)

# papers = [0, 5, 5, 5, 5, 5]
# answer = 0


# def get_areas() :
#     results = []
#     for i in range(len(spots)) :
#         og_x, og_y = spots[i]
#         x, y = og_x, og_y
#         while y < 9 :
#             # print("checking y (", og_x, y, ")")
#             if arr[og_x][y+1] == 1 : y +=1
#             else : 
#                 # print("y확정", y, "최대 n", y-og_y+1)
#                 break
#         while x-og_x+1 < y-og_y+1 and x < 9 :
#             # print("checking x (", x, og_y, ")")
#             if arr[x+1][og_y] == 1 : x += 1
#             else :
#                 # print("x확정", x, "n 확정", x-og_x+1) 
#                 break
#         # print("results append", [x-og_x+1, og_x, og_y])
#         results.append([x-og_x+1, og_x, og_y])

#     return results

# while sum(papers) > 0 :
#     # 구역 파악해서 pq에 넣기
#     areas = get_areas()
#     if not areas : break
#     else :
#         pq = []
#         for area in areas :
#             if area[0] <= 5 :
#                 heapq.heappush(pq, [-area[0], area[1], area[2]])

#     n, x, y = heapq.heappop(pq)
#     for r in range(x, x - n) :
#         for c in range(y, y - n) :
#             arr[r][c] = 0
#             spots.remove([r, c])
#     papers[-n] -= 1
#     answer += 1

# print(answer)
