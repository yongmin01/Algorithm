# [백준] 백트래킹 > 좋은수열

N = int(input())
answer = 0
def backtracking(seq) :
    global answer, N
    if len(seq) == N :
        print(seq)
        exit()
    else :
        for n in ['1', '2', '3'] :
            new_seq = seq + n
            for l in range(1, len(new_seq)//2+1) :
                if new_seq[-l*2:-l] == new_seq[-l:] : 
                    break
            else :
                backtracking(new_seq)

backtracking('1')
