# [백준] 그래프 탐색(BFS, 최단경로, 0-1 너비 우선 탐색) > 숨바꼭질 3

# 다익스트라 풀이
import heapq
from collections import defaultdict

n, k = map(int, input().split())

# n > k인 경우에 n이 k에 도달하기 위해서는 -1만 가능
if n >= k : 
    print(n-k)
    exit()

pq = []
INF = int(1e9)
visited = defaultdict(lambda: INF)

heapq.heappush(pq, (0, n))
while pq :
    time, pos = heapq.heappop(pq)
    
    if pos == k : # 우선순위 큐를 사용했기 때문에 최단 시간이 보장되므로 pos가 k라면 바로 출력 가능
        print(time)
        exit()

    if visited[pos] < time : continue # 해당 위치에 도달하는 더 짧은 경로가 이미 존재하므로 pass
    if pos > k : # 위에서와 마찬가지로 수빈이의 위치가 동생보다 큰 경우에는 -1만 가능한데 이때도 최단 시간인 경우에만 push
        if time + 1 < visited[pos-1] :
            visited[pos-1] = time + 1
            heapq.heappush(pq, (visited[pos-1], pos-1))
    else :
        cand = [pos*2, pos-1, pos+1]
        for c in cand :
            if -1 < c <= 100000 :
                if c == pos*2 :
                    if time < visited[c] :
                        visited[c] = time
                        heapq.heappush(pq, (time, c))
                else :
                    if time + 1 < visited[c] :
                        visited[c] = time + 1
                        heapq.heappush(pq, (time+1, c))

# BFS 풀이
from collections import deque
from collections import defaultdict

n, k = map(int, input().split())
INF = int(1e9)
visited = defaultdict(lambda: INF)

q = deque()
q.append((n, 0))

while q :
    pos, time = q.popleft()
    if pos == k : 
        print(time)
        exit()
    cand = [pos*2, pos-1, pos+1]
    for c in cand :
        if c == pos*2 :
            if 0 <= c < 100001 and time < visited[c] :
                visited[c] = time 
                q.appendleft((c, time))
        else :
            if 0 <= c < 100001 and time+1 < visited[c] :
                visited[c] = time
                q.append((c, time+1))