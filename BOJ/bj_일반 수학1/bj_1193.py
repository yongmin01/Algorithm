X = int(input())
y = 1
diagonal = 1
while X > y :
    diagonal += 1
    y += diagonal

row = 1
conlumn = diagonal
z = y - diagonal + 1
while X != z :
    row += 1
    conlumn -= 1
    z += 1
if diagonal % 2 == 0 :
    print(str(row)+ "/" + str(conlumn))
else :
    print(str(conlumn) + "/" + str(row))