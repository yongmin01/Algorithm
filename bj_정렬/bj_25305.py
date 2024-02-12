# 백준 정렬_3 : 커트라인
[N, k] = [int(_) for _ in input().split()]
scores = [int(x) for x in list(input().split())]
scores.sort(reverse=True)
print(scores[k-1])