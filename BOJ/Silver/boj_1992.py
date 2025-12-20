# [백준] 분할 정복 > 쿼드트리

import sys
input = sys.stdin.readline

N = int(input())
video = []
for _ in range(N) :
    video.append(list(map(int, input().strip())))

answer = []
def quad_tree(x, y, n) :
    color = video[x][y]
    for r in range(x, x+n) :
        for c in range(y, y+n) :
            if color != video[r][c] :
                answer.append('(')
                quad_tree(x, y, n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                answer.append(')')
                return
    answer.append(color)
quad_tree(0, 0, N)
print(''.join(map(str, answer)))