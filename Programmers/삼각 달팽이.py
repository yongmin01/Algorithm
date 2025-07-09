# [프로그래머스] 삼각 달팽이

def solution(n):
    answer = []
    tri = []
    for i in range(1, n+1) :
        tri.append([0 for _ in range(i)])
        
    cur = 1
    i , j = 0, 0
    while cur <= n * (n+1) // 2 :
        # 왼변
        while i < n and tri[i][j] == 0 :
            tri[i][j] = cur
            i += 1
            cur += 1
        i -= 1
        j += 1
        # 밑변
        while j < n and tri[i][j] == 0 :
            tri[i][j] = cur
            j += 1
            cur += 1
        j -= 2
        i -= 1
        # 오른변
        while i > 0 and j > 0 and tri[i][j] == 0 :
            tri[i][j] = cur
            i -= 1
            j -= 1
            cur += 1
        i += 2
        j += 1
        
    for li in tri :
        answer.extend(li)
        
    return answer