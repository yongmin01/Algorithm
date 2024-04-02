# 백준 재귀_3 : 재귀의 귀재

import sys
N = int(sys.stdin.readline())
def recursion (s, l, r, count) :
    if (l >= r) : 
        print(1, count)
        return 1
    elif (s[l] != s[r]) : 
        print(0, count)
        return 0
    else : 
        count += 1
        recursion(s, l+1, r-1, count)

def isPalidrome(s) :
    return recursion(s, 0, len(s) - 1, 1)
    

for i in range(N) :
    s = sys.stdin.readline().rstrip()
    isPalidrome(s)
    
