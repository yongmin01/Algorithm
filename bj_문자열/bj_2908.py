A, B = [x for x in input().split()]
print(max(int(A[::-1]), int(B[::-1])))