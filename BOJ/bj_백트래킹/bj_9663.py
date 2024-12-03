# 백준 백트래킹_5 : N-Queen
# Python3로 제출하면 시간초과, PyPy3로 제출하면 정답.. 시간 복잡도 줄이는 코드도 다시 생각해보기

import sys
input = sys.stdin.readline
N = int(input())
sol = 0


def queens(N, row, current_candidate) :
    global sol
    if row == N : 
        sol +=1
        return
    
    for col in range(N) :
        if promissing(current_candidate, col, row) :
            current_candidate.append(col)
            queens(N, row+1, current_candidate)
            current_candidate.pop()


def promissing(candidate, col, row) :
    for i in range(row) :
        if candidate[i] == col or abs(candidate[i] - col) == row - i :
            return False
    return True

queens(N, 0, [])
print(sol)


# 처음 생각한 코드

# N = int(input())
# sol = 0
# cols = [0 for i in range(N)]


# def queens(row) :
#     global sol
#     if row == N : 
#         sol += 1
#         return
#     for col in range(N) :
#         if promissing(col, row) :
#             cols[col] = row
#             queens(row+1)
#     cols[cols.index(row-1)] = 0
#     queens(row-1)


# def promissing(col, row) :
#     if cols[col] != 0: return False
#     for i in cols :
#         if abs(cols.index(i) - i) == abs(col - row) : return False
#     return True

# queens(N)
# print(sol)