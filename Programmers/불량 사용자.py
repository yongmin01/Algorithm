# [프로그래머스] 2019 카카오 개발자 겨울 인턴십 > 불량 사용자

from collections import defaultdict

def solution(user_id, banned_id):
    answer = set()
    bid_dict = defaultdict(set)
    for uid in range(len(user_id)) :
        for bid in range(len(banned_id)) :
            if len(user_id[uid]) == len(banned_id[bid]) :
                for i in range(len(banned_id[bid])) :
                    if banned_id[bid][i] != '*' and user_id[uid][i] != banned_id[bid][i] : break
                else : bid_dict[bid].add(uid)

    def dfs(depth, acc) :
        nonlocal answer
        if depth == len(banned_id) :
            #answer.add(acc) 
            # set은 mutable -> unhashable하기 때문에 set의 원소로 쓰일 수 없음
            #answer.add(list(acc)) 
            # list도 mutable -> unhashable 하기 때문에 set의 원소로 쓰일 수 없음
            
            # answer.add(tuple(acc)) 
            # 그래서 hashable한 tuple로 변환해서 추가하려고 하면 (0, 1, 2), (1, 2, 0)처럼 같은 원소로 여겨져야 할 목록이 순서를 가져서 다른 조합으로 취급될 수 있음
            # answer.add(tuple(sorted(acc))) 
            # 정렬 후 tuple로 만들어서 원소의 순서를 보장하거나
            answer.add(frozenset(acc)) 
            # fronzenset을 통해 set을 hasable하게 만들어서 set에 추가 가능하게 함
            # frozenset은 set의 immutable 버전으로 hashable 자료형
            return
        for choice in list(bid_dict[depth]) :
            if choice not in acc :
                acc.add(choice)
                dfs(depth+1, acc)
                acc.remove(choice)
    dfs(0, set())
    return len(answer)
        