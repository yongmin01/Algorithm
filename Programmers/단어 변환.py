# [프로그래머스] 깊이/너비 우선 탐색(DFS/BFS) > 단어 변환

from collections import deque

def comp(word, target) :
    count = 0
    for w in range(len(word)) :
        if word[w] != target[w] :
            count += 1
    if count <= 1 :
        return True
    else : return False

def solution(begin, target, words):
    answer = 0
    
    visited = [False] * (len(words)+1)
    q = deque()
    q.append((begin, 0, len(words)))
    while q :
        word, count, index = q.popleft()
        visited[index] = True
        if word == target :
            answer = count
            break
        for i in range(len(words)) :
            if visited[i] == False and comp(word, words[i]):
                q.append((words[i], count+1, i))
    return answer