def solution() :
    N = int(input())
    numbers = [int(x) for x in input().split()]
    v = int(input())
    count = 0
    for x in numbers:
        if ( x == v):
            count += 1
    return count

print(solution())
