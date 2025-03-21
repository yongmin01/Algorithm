# 백준_그리디 알고리즘 : 단어 수학

import sys
input = sys.stdin.readline

N = int(input())
words = []
max_length = 0 # 가장 긴 단어의 길이

# 단어 입력
for _ in range(N) :
    word = input().rstrip()[::-1] # 단어는 거꾸로 저장 ABC -> CBA
    words.append(word)
    if len(word) > max_length :
        max_length = len(word)

# 각 알파벳이 각 자리수별로 몇 개 있는지 저장하는 리스트
digits = [[0 for _ in range(26)] for _ in range(max_length+1)]

for word in range(N) :
    for a in range(len(words[word])) :
        digits[a][ord(words[word][a])-65] += 10 ** (a+1) # 10 ** (자릿수) 값을 가중치로 매겨서 저장
        digits[max_length][ord(words[word][a])-65] += 1 # 마지막 요소에는 각 알파벳의 등장 횟수를 저장


# 각 알파벳들의 최종 가중치 구하기 (등장한 알파벳만 저장하기 위해 if문 처리)
results = []
for alphabet in range(26) :
    val = 0
    for digit in range(max_length) :
        val += digits[digit][alphabet]
    if val != 0 :
        results.append((val, alphabet))

# 가중치가 높은 순서로 정렬 후 각 알파벳에 0~9 부여
results.sort(reverse=True) 
order = 9
priority = [0 for _ in range(26)]
for pri in results :
    priority[pri[1]] = order
    order -= 1

# 단어를 순회하면서 단어를 수로 변환
answer = 0
for word in words :
    temp = ''
    for alphabet in range(len(word)-1, -1, -1) :
        temp += str(priority[ord(word[alphabet]) - 65])
    answer += int(temp)
print(answer)