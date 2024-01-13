N = int(input())

count = 0
for i in range(N) :
    word = input()
    temp = []
    if len(word) == len(set(word)) :
        count += 1
    else :
        result = True
        for x in range(len(word)) :
            if word[x] not in temp :
                temp.append(word[x])
            else :
                if word[x - 1] != word[x] : 
                    result = False
                    break
        if result != False : 
            count += 1
print(count)
                

