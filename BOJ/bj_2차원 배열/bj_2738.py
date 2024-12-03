N, M = [int(x) for x in input().split()]
A = []
B = []

for n in range(N) :
    A.append([int(x) for x in input().split()])
for m in range(N) :
    B.append([int(x) for x in input().split()])

for n in range(N) :
    for m in range(M) :
        print(A[n][m] + B[n][m], end=" ")
    print()
        
