subject = int(input())
scores = [int(x) for x in input().split()]
M = max(scores)
for x in range(len(scores)) :
    scores[x] = scores[x]/M*100

print(sum(scores)/len(scores))