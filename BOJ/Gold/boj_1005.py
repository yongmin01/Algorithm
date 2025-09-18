# [백준] 위상 정렬 > ACM Craft

import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for t in range(T) :
    n, k = map(int, input().split())
    buildings = deque(map(int, input().split()))
    buildings.appendleft(0)
    
    inorder = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    for i in range(k) :
        b1, b2 = map(int, input().split())
        inorder[b2] += 1
        graph[b1].append(b2)
    
    target = int(input())

    q = deque()
    # 시작 지점 찾아서 (지점, depth=0)으로 세팅
    for i in range(1, n+1) :
        if inorder[i] == 0 : q.append((i, 0))
    
    temps = [[] for _ in range(n+1)]
    while q :
        curr, depth = q.popleft()

        for next in graph[curr] :
            inorder[next] -= 1
            temps[next].append(buildings[curr])
            
            if inorder[next] == 0 :
                buildings[next] += max(temps[next])
                q.append((next, depth+1))

    print(buildings[target])
