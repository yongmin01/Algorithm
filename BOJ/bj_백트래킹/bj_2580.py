# 백준 백트래킹_6 : 스도쿠
# Python3로 제출하면 시간초과, PyPy3로 제출하면 정답.. 시간 복잡도 줄이는 코드도 다시 생각해보기

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