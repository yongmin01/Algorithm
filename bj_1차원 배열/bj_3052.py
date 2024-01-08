remainders = []
count = 0
for x in range(10) :
    remainder = int(input()) % 42
    if ((remainder in remainders) == False) :
        remainders.append(remainder)
        count += 1
print(count)