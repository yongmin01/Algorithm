# 백준 백트래킹_1 : N과 M (1)
s = []
def back(n, m) :
    if len(s) == m :
            print(" ".join(map(str, s)))
            return
    for i in range(1, n+1) :
        if i not in s :
            s.append(i)
            back(n, m)
            s.pop()
            
[N, M] = map(int, input().split())
back(N, M)