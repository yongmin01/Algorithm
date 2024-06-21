# 백준 백트래킹_3 : N과 M (3)
result = []

def pick(n, m) :
    if len(result) == m :
        print(" ".join(map(str, result)))
        return
    for i in range(1, n+1) :
        result.append(i)
        pick(n, m)
        result.pop()

[N, M] = map(int, input().split())
pick(N, M)