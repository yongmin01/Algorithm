# # [백준] 정렬 > 강의실 배정

# queue 모듈의 PriorityQueue로 풀이시 [메모리 : 81368KB, 시간 : 832ms]
# import sys
# from queue import PriorityQueue
# input = sys.stdin.readline

# N = int(input())
# classes = []
# for _ in range(N) :
#     classes.append(tuple(map(int, input().split())))

# classes = sorted(classes, key=lambda c : (c[0], c[1]))

# pq = PriorityQueue()
# answer = 1
# earlest_end_class = classes[0][1]
# for c in classes[1:] :
#     start, end = c
#     if start >= earlest_end_class :
#         pq.put(end)
#         earlest_end_class = pq.get()
#     else :
#         answer += 1
#         pq.put(end)
#         pq.put(earlest_end_class)
#         earlest_end_class = pq.get()
# print(answer)

# heapq로 풀이 시 [메모리 : 77088KB, 시간 : 336ms]
import sys
import heapq
input = sys.stdin.readline

N = int(input())
classes = []
for _ in range(N) :
    classes.append(tuple(map(int, input().split())))

classes = sorted(classes, key=lambda c : (c[0], c[1]))

pq = []
answer = 1
heapq.heappush(pq, classes[0][1])
for c in classes[1:] :
    start, end = c
    if start >= pq[0] :
        heapq.heappop(pq)
        heapq.heappush(pq, end)
    else :
        answer += 1
        heapq.heappush(pq, end)
print(answer)