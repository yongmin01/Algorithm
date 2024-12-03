import string
num, notation = input().split()
result = 0
count = 0
aList = list(string.ascii_uppercase)
for x in num :
    if x not in aList :
        result = result + int(x)*int(notation)**(len(num)-count-1)
        count += 1
    else :
        result = result + (aList.index(x)+10)*int(notation)**(len(num)-count-1)
        count += 1
print(result)
