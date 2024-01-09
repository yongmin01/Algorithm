word = input()
dial = [0, 0, ['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'], ['T','U','V'], ['W','X','Y','Z']]
result = []
for x in range(len(word)) :
    for y in range(2, 10) :
        if (word[x] in dial[y]) :
            result.append(y)
print(sum(result)+len(word))