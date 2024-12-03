# 백준 심화 2_2 : 인사성 밝은 곰곰이

import sys
N = int(sys.stdin.readline().rstrip())
enter =[]
gomgom = 0
for i in range(N) :
    chat = sys.stdin.readline().rstrip()
    if chat == "ENTER" :
        gomgom += len(set(enter))
        enter = []
    else : 
        enter.append(chat)

set(enter)
print(len(set(enter)) + gomgom)