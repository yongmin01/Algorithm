# [프로그래머스] 여행경로

from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)
    for dep, arri in tickets :
        routes[dep].append(arri)
    for city in routes.values() :
        city.sort()
    
    cityAmount = len(tickets) + 1
    temp = []
    
    def dfs(city) :
        nonlocal answer
        if len(temp) == cityAmount : 
            if len(answer) == 0 : answer = temp[:]
            return
        for i in range(len(routes[city])) :
            if routes[city][i] :
                destination = routes[city][i]
                temp.append(destination)
                routes[city][i] = False
                dfs(destination)
                temp.pop()
                routes[city][i] = destination
    
    temp.append("ICN")     
    dfs("ICN")
    
    return answer
        