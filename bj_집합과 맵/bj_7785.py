# 백준 집합과 맵_3 : 회사에 있는 사람
import sys
n = int(sys.stdin.readline())
log = {}
for i in range(n) :
    [name, status] = list(sys.stdin.readline().split())
    log[name] = status

log_sorted = sorted(log, reverse=True)

for i in log_sorted :
    if (log[i] == "enter") :
        print(i)