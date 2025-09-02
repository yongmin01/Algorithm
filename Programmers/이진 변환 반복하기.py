# [프로그래머스] 이진 변환 반복하기

# from collections import deque 

# def solution(s):
#     answer = [0, 0]
    
#     def recursion(m) :
#         if len(m) == 1 and m[0] == 1 :
#             return
#         else :
#             answer[0] += 1
#             m_length = 0
#             for n in m :
#                 if n == 0 :
#                     answer[1] += 1
#                 else : m_length += 1
            
#             a = m_length
#             q = deque()
#             while a > 1 :
#                 q.append(a % 2)
#                 a = a // 2
#             q.appendleft(1)
#             recursion(list(q))
                  
#     recursion(list(map(int, s)))
        
#     return answer

def solution(s) :
    a, b = 0, 0
    while s != '1' :
        a += 1
        b += s.count('0')
        s = bin(s.count('1'))[2:] # bin 함수의 반환값은 변환된 이진수 앞에 0b가 붙은 형태이므로 앞에 두 글자는 제외해야 함 ex) bin(7) -> '0b111'
    return [a, b]