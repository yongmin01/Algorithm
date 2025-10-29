# [프로그래머스] 2025 프로그래머스 코드챌린지 2차 예선 > 완전범죄

def solution(info, n, m):
    size = len(info)
    answer = 121
    comb = set()
    
    def check(asum, bsum, i) :
        nonlocal answer
        if asum >= n or bsum >= m : # 흔적을 남겨서 잡히는 경우
            return
        
        if (asum, bsum, i) in comb : # 이미 확인한 조합인 경우
            return
        
        comb.add((asum, bsum, i)) # (A의 누적 흔적 개수, B의 누적 흔적 개수, 몇번째 물건까지 훔쳤는지)를 조합으로 경우의 수 확인
        
        if i == size :
            answer = min(answer, asum)
            return
        
        check(asum+info[i][0], bsum, i+1) # i+1번째 물건을 A가 훔치는 경우
        check(asum, bsum+info[i][1], i+1) # i+1번째 물건을 B가 훔치는 경우
        
    check(0, 0, 0)
    
    return answer if answer != 121 else -1
            