sentance = input()
count = 1
for x in range(len(sentance)) :
    if (sentance[x] == " ") :
        count += 1
if (sentance[0] == " ") :
    count -= 1
if (sentance[-1] == " ") :
    count -= 1
print(count)