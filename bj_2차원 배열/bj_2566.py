matrix = []
max_val = 0
max_position  = 0
for x in range(9) :
    matrix.append([int(num) for num in input().split()])

for x in range(9) :
    if max(matrix[x]) >= max_val : # 등호 필수!
        max_val = max(matrix[x])
        max_position = [x, matrix[x].index(max_val)]
print(max_val)
print(max_position[0] + 1, max_position[1] + 1)
