# [프로그래머스] > 과제 진행하기

from collections import defaultdict, deque

def solution(plans):
    answer = []
    schedule = []
    duration = defaultdict(int)
    
    for plan in plans :
        start = int(plan[1].split(":")[0]) * 60 + int(plan[1].split(":")[1])
        schedule.append([plan[0], start])
        duration[plan[0]] = int(plan[2])
        
    # 시작 시간을 분으로 바꿔서 시작 시간이 작은(빠른) 순으로 정렬    
    schedule.sort(key=lambda x : x[1])
    
    q = deque() # 아직 끝내지 못한 과제들
    q.append(schedule[0])
    cur_time = schedule[0][1] # 현재 시간
    for plan in schedule[1:] :
        cur_sub, cur_start_time = plan # 새로 주어진 과제
        while q :
            prev_sub, prev_start_time = q[-1] # 아직 끝내지 못한 과제 중 가장 최근 과제
            if cur_start_time >= cur_time + duration[prev_sub] : # 가장 최근 과제를 끝낼 시간이 충분한 경우
                cur_time += duration[prev_sub] # 현재 시간에 과제를 끝나는데 걸리는 시간을 더해서 업데이트
                answer.append(prev_sub) # 과제를 끝냄
                q.pop()
                
            else :
                duration[prev_sub] -= cur_start_time - cur_time # 과제를 끝내지는 못하지만 여유 시간만큼 최대한 수행
                cur_time = cur_start_time
                q.append(plan)
                break
        else : # 끝내지 못한 과제가 없는 경우 현재 과제를 대기열에 추가
            q.append(plan) 
            cur_time = cur_start_time
    while q : # 마지막 과제를 끝내고 남은 과제는 최신순으로 수행
        cur_sub, _ = q.pop()
        answer.append(cur_sub)
                
    return answer