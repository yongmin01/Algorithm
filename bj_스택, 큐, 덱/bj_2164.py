# 백준 스택, 큐, 덱_7 : 카드2
import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque(list(range(1, N + 1)))

while len(queue) != 1 :
    del queue[0]
    queue.append(queue[0])
    del queue[0]
print(queue[0])
