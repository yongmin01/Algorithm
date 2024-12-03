# 백준 심화 2_5 : 영단어 암기는 괴로워
import sys
[N, M] = list(map(int, sys.stdin.readline().split()))
vocas = {}
for i in range(N) :
    voca = sys.stdin.readline().rstrip()
    if len(voca) >= M :
        if voca in vocas.keys():
            vocas[voca] += 1
        else :
            vocas[voca] = 1


sortedVocas = sorted(vocas.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in range(len(sortedVocas)) :
    print(sortedVocas[i][0])
