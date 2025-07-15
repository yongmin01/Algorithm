# [프로그래머스] > 롤케이크 자르기

def solution(topping):
    answer = 0
    
    철수_set = set()
    brother_set = set()
    
    철수 = []
    brother = []
    
    for i in range(len(topping)) :
        철수_set.add(topping[i])
        brother_set.add(topping[-(i+1)])
        철수.append(len(철수_set))
        brother.append(len(brother_set))
    
    brother = brother[::-1]
    
    for i in range(len(topping)-1) :
        if 철수[i] == brother[i+1] :
            answer += 1
    
    return answer