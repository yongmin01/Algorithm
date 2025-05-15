# [프로그래머스] 깊이/너비 우선 탐색(DFS/BFS) > 타겟넘버

answer = 0
def dfs(idx, cur, numbers, target) :
    global answer
    if idx == len(numbers) :
        if cur == target :
            answer += 1
        return answer
    dfs(idx + 1, cur+numbers[idx], numbers, target)
    dfs(idx + 1, cur-numbers[idx], numbers, target)
    return answer

def solution(numbers, target):
    return dfs(0, 0, numbers, target)