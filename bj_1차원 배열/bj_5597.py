students = []
for x in range(30) :
    students.append(x+1)

for y in range(28) :
    good_student = int(input())
    students.remove(good_student)
    
print(students[0])
print(students[1])
