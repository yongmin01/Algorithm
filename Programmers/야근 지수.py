# [프로그래머스] 야근 지수

import heapq 
def solution(n, works):
    answer = 0
    pq = []
    for work in works :
        heapq.heappush(pq, (-work, work))

    while n > 0 and pq :
        _, work = heapq.heappop(pq)
        if work == 0 : continue
        work -= 1
        heapq.heappush(pq, (-work, work))
        n -= 1
    
    while pq :
        _, work = heapq.heappop(pq)
        answer += work ** 2
        
    return answer