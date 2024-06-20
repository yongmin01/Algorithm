# 백준 백트래킹_1 : N과 M (2)
s = []
def dfs (start, n, m) :
    if len(s) == m :
            print(" ".join(map(str, s)))
            return
    for i in range(start, n+1) :
        if i not in s :
                s.append(i)
                dfs(i+1, n, m)
                s.pop()
    
[N, M] = map(int, input().split())
dfs(1, N, M)
