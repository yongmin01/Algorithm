crotia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
start_index_list = []
for x in crotia :
    if x in word :
        word = word.replace(x, "*")
print(len(word))