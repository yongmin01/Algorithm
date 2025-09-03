# [백준] 백트래킹 > N-Queen

# python3는 시간 초과, pypy는 통과

n = int(input())

answer = 0
cols = [-1] * n

def dfs(cur_row, cols) :
    global answer
    if cur_row == n : # 현재 검사해야 할 행이 n이 됐다는 것은 (0 ~ n-1) => n개의 행에 모두 퀸을 배치했다는 뜻
        answer += 1
        return
    
    for candidate_col in range(n) : # 현재 행의 몇번째 열에 말을 둘지 
        cols[cur_row] = candidate_col
        if promissing(cur_row, candidate_col, cols) :
            dfs(cur_row+1, cols)
    return
        

def promissing(cur_row, cur_col, cols) : # 현재 행(cur_row), 현재 열(cur_col)의 위치에 말을 놓아도 되는지 결정하기 위해
    for past_row in range(cur_row) : # 현재행-1까지의 말들을 순회
        if cols[past_row] == cur_col or abs(cur_col - cols[past_row]) == abs(cur_row - past_row) :
            return False

    return True


dfs(0, cols)
print(answer)


# python3도 통과하는 코드 (해당 위치가 유망한지 검사를 O(n)이 아닌 O(1)에 수행)

import sys
input = sys.stdin.readline

n = int(input())
col = [False] * n # 열 검사
diag1 = [False] * (2 * n - 1) # / 대각선 검사용
diag2 = [False] * (2 * n - 1) # \ 대각선 검사용
answer = 0

def dfs(row):
    global answer
    if row == n:  # 0 ~ n-1 행(n개)에 모두 퀸 배치 완료
        answer += 1
        return
    
    for c in range(n):
        print(row, c)
        if not col[c] and not diag1[(n-1) - c + row] and not diag2[row + c]: # 열, / 대각선, \ 대각선 모두 비어있는지 O(1)에 확인
            col[c] = diag1[(n-1) - c + row] = diag2[row + c] = True # 배치가 가능한 위치면 -> 검사용 배열 모두 업데이트
            dfs(row + 1)
            col[c] = diag1[(n-1) - c + row] = diag2[row + c] = False # 배치 철회

dfs(0)
print(answer)
