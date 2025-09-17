# [프로그래머스] > 연속된 부분 수열의 합

def solution(sequence, k):
    result = []
    s = e = 0
    acc = sequence[s]
    
    while s < len(sequence) and e < len(sequence) :
        if acc < k : # acc가 k보다 작을 경우 end 늘리기
            e += 1
            if e < len(sequence) : # 인덱스 범위를 넘지 않는지 체크
                acc += sequence[e]
                
        elif acc == k : # acc가 k일경우 result 갱신
            if len(result) == 0 : result = [s, e]
            else :
                if e - s < result[1] - result[0] :
                    result = [s, e]
                elif e - s == result[1] - result[0] :
                    result = [s, e] if s < result[0] else result
            e += 1 # result 갱신 후 end를 늘려서 acc 갱신
            if e < len(sequence) : 
                acc += sequence[e]
                
        else : # acc가 k보다 큰 경우 start 밀기
            if s < len(sequence) : acc -= sequence[s] # 인덱스 범위를 넘지 않는지 체크
            s += 1
                
    return result