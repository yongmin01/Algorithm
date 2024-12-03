word = input()
if len(word) % 2 == 0 :
    back = word[-1 : len(word)//2-1 : -1] 
    if (word[:len(word)//2] == back) :
        print(1)
    else : print(0)
else :
    back = word[-1 : len(word)//2 : -1]
    if (word[:len(word)//2] == back) :
        print(1)
    else : print(0)