# [백준] 브루트포스 > 암호 만들기

import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
alphabets = list(input().split())

all_vowel = ['a', 'e', 'i', 'o', 'u']
vowel = []
consonant = []

for al in alphabets :
    if al in all_vowel :
        vowel.append(al)
    else : consonant.append(al)

answer = []
for i in range(1, len(vowel)+1) :
    if 2 <= L - i <= len(consonant) :
        for v in combinations(vowel, i) :
            for c in combinations(consonant, L-i) :
                s = sorted(list(v+c))
                answer.append(''.join(s))
answer.sort()
for s in answer :
    print(s)
