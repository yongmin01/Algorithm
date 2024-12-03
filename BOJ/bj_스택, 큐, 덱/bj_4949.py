# 백준 스택, 큐, 덱_4 : 균형잡힌 세상
import sys
while True:
    s = sys.stdin.readline().rstrip()
    if len(s) == 1 and s == "." :
        break
    bracket = []
    for i in s :
        if i == "." : 
            if len(bracket) == 0:
                print("yes")
            else :
                print("no")
        else:
            if i == "(" or i == "[" :
                bracket.append(i)
            elif i == ")":
                if len(bracket) != 0 and bracket[-1] == "(" :
                    bracket.pop()
                else:
                    print("no")
                    break
            elif i == "]" :
                if len(bracket) != 0 and bracket[-1] == "[" :
                    bracket.pop()
                else:
                    print("no")
                    break
            elif i == "]" :
                if bracket[-1] == "[" :
                    bracket.pop()
                else :
                    print("no")
                    break
            else : continue