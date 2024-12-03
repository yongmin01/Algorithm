# 백준 재귀_7 : 하노이 탑 이동 순서
def hanoi(amount, start, mid, end) :
    if amount == 1 : 
        print(start, end)
        return True
    hanoi(amount-1, start, end, mid)
    print(start, end)
    hanoi(amount-1, mid, start, end)


N = int(input())
print(2**N -1)
hanoi(N, 1, 2, 3)