# [백준] 구현, 자료구조 > 뱀

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
k = int(input())

# 보드에 사과 위치 표시
board = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k) :
  r, c = map(int, input().split())
  board[r-1][c-1] = 'a'

# 뱀의 초기 위치 표시
board[0][0] = 'b'

# 방향 변환 정보 저장
l = int(input())
direction_controls = deque()
for _ in range(l) :
  t, d = input().split()
  direction_controls.append((int(t), d))

directions = deque() # 방향 변환 이력

d = (0, 1) # 현재 향하는 방향
directions.append(d)
time = 1
head = [0, 0]
tail = [0, 0]
dt, nd = direction_controls.popleft() # 다음 방향 전환 시간, 전환할 방향

while True:
  head = [head[0]+d[0], head[1]+d[1]] # 머리 이동
  # 종료되는 경우
  if head[0] < 0 or head[0] >= n or head[1] < 0 or head[1] >= n : # 머리가 벽과 만나는 경우
    print(time)
    exit()
  if board[head[0]][head[1]] == 'b' : # 몸통과 머리가 만나는 경우
    print(time)
    exit()

  # 종료되지 않는 경우
  if board[head[0]][head[1]] != 'a' : # 사과를 만나지 않으면 꼬리를 당겨옴 (사과를 만나면 꼬리 이동 X)
    board[tail[0]][tail[1]] = 0 # 꼬리가 있던 자리 표시 지우기
    di = directions.popleft()
    tail = [tail[0]+di[0], tail[1]+di[1]] # 몸통이 향하던 방향에 맞게 꼬리 이동
  board[head[0]][head[1]] = 'b' # 머리 이동
  
  # 방향 전환
  if time == dt :
    x, y = d
    if x == 0 and y == 1 : # 오른쪽을 향하다가
      if nd == 'L' : x, y = -1, 0 # -> 위쪽을 향하게 됨
      else : x, y = 1, 0 # -> 아래쪽을 향하게 됨

    elif x == 1 and y == 0 : # 아래쪽을 향하다가
      if nd == 'L' : x, y = 0, 1 # -> 오른쪽을 향하게 됨
      else : x, y = 0, -1 # -> 왼쪽을 향하게 됨

    elif x == 0 and y == -1 : # 왼쪽을 향하다가
      if nd == 'L' : x, y = 1, 0 # -> 아래쪽을 향하게 됨
      else : x, y = -1, 0 # -> 위쪽을 향하게 됨

    elif x == -1 and y == 0 : # 위쪽을 향하다가
      if nd == 'L' : x, y = 0, -1 # -> 왼쪽을 향하게 됨
      else : x, y = 0, 1 # -> 오른쪽을 향하게 됨

    d = (x, y) # 향하는 방향 갱신

    if direction_controls : # 방향 전환 횟수가 남은 경우에만 다음 전환할 방향 업데이트
      dt, nd = direction_controls.popleft()
  directions.append(d) # 방향 전환 이력 추가
  time += 1

