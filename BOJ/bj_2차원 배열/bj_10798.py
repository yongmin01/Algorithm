words = []
max_len = 0
for x in range(5) :
    word = input()
    words.append(word)
    if len(word) >= max_len :
        max_len = len(word)

for x in range(max_len) :
    for y in range(5) :
        try:
            print(words[y][x], end='')
        except IndexError :
            y += 1
