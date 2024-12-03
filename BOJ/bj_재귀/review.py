N = int(input())

def hanoi(amount, start, mid, end) :
    if amount == 1:
        print(start, mid)
        return
    hanoi(amount-1, start, end, mid)
    print(start, end)
    hanoi(amount-1, mid, start, end)
hanoi(N, 1, 2, 3)



# 2580번(백트래킹6)
import sys
input = sys.stdin.readline
# 입력받기
nums =  [list(map(int, input().split())) for _ in range(9)]

# 빈칸 모으기
Blank = []
def getBlank() :
    for i in range(9) :
        for l in range(9) :
            if nums[i][l] == 0 :
                Blank.append([i, l])
    return

    # 행 체크
def checkRow(n, row) : 
    if n in nums[row] : return False
    return True

def checkCol(n, col) :
    # 열 체크
    for i in range(9) :
        if n == nums[i][col] : return False
    return True

def checkBox(n, row, col) :
    # 3*3 체크
    for r in range(3) :
        for c in range(3) :
            if n == nums[row//3*3 + r][col//3*3 + c] : return False
    return True

def isPromissing(n, row, col) :
    if checkRow(n, row) and checkCol(n,col) and checkBox(n, row, col) :
        return True
    return False

def numberPlace(blank) :
    if blank == len(Blank) :
        for i in range(9) :
            print(" ".join(map(str, nums[i])))
        exit()
    for n in range(1, 10) :
        if isPromissing(n, Blank[blank][0], Blank[blank][1]) :
            nums[Blank[blank][0]][Blank[blank][1]] = n
            numberPlace(blank+1)
            nums[Blank[blank][0]][Blank[blank][1]] = 0
            

getBlank()
numberPlace(0)

# makeSquare()
# 3*3 구역 나누기
square = []
def makeSquare() :
    i = 0
    for a in range(0, 9, 3) :
        for b in range(0, 9, 3) :
            temp = []
            for i in range(a, a + 3) :
                for l in range(b, b + 3) :
                    temp.append(nums[i][l])
            square.append(temp)
    return 




