# 백준 백트래킹_4 : N과 M (4) 
L = []
def list (start, n, m) :
    if len(L) == m : 
        print(" ".join(map(str, L)))
        return
    for i in range(start, n+1) :
        L.append(i)
        list(i, n, m)
        L.pop()
    

[N, M] = map(int, input().split())
list(1, N, M)