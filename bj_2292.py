N = int(input())
x = 1
count = 1
while N > x+6*count :
    x = x + 6*count
    count += 1
if N == 1 :
    print(1)
else : 
    print(count + 1)