max = 0
index = 0
nums = []
for x in range(9) :
    nums.append(int(input()))

for x in range(9) :
    if (nums[x] > max) : 
        max = nums[x]
        index  = x
print(max)
print(index + 1)