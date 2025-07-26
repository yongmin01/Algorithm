# [백준] 조합론 > 로또

from itertools import combinations

while True :
    testcase = list(map(int, input().split()))
    if testcase[0] == 0 : break
    k, s = testcase[0], testcase[1:]
    comb = combinations(s, 6)
    for c in comb :
        print(' '.join(map(str, sorted(c))))
    print()
