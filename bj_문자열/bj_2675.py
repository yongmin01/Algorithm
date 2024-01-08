T = int(input())
for n in range(T) :
    R, S = [x for x in input().split()]
    result = []
    for x in range(len(S)) :
        result.append(S[x]*int(R))
    print("".join(result))
        