# 백준_시뮬레이션 : 프린터 큐

import sys
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    N, M = map(int, input().split())
    queue = deque()
    pq = PriorityQueue()
    docs = list(map(int, input().split()))

    for i in range(N) :
        queue.append((docs[i], i)) # (중요도, 인덱스)
        pq.put((-docs[i], docs[i])) # (우선순위(== -중요도), 중요도)
    answer = 0
    while True :
        front = queue.popleft()
        pq_top = pq.get()
        if front[0] == pq_top[1] :
            answer += 1
            if front[1] == M : 
                print(answer)
                break
        else : 
            queue.append(front)
            pq.put(pq_top)
