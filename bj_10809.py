from string import ascii_lowercase

word = input()
result = list(ascii_lowercase)

for x in range(len(result)) :
    if (result[x] in word) :
        result[x] = word.index(result[x])
    else : result[x] = -1

for x in result :
    print(x, end=" ")