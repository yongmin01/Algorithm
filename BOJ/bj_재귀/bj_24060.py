# 백준 재귀_4 : 알고리즘 수업 - 병합 정렬 1
# 다시 풀기

N, K = list(map(int, input().split()))

nums = list(map(int, input().split()))
cnt = 0
result = -1

def merge_sort(arr, p, r) :
    if p < r and cnt <= K :
        q = (p + r)// 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+ 1, r)
        merge(arr, p, q, r)



def merge(A, p, q, r) :
    i = p
    j = q + 1
    t = 1
    temp = []
    global cnt, result
    while i <= q and j <= r :
        if A[i] <= A[j] :
            temp.append(A[i])
            i += 1
        else : 
            temp.append(A[j])
            j += 1
    while i <= q :
        temp.append(A[i])
        i += 1
    while j <= r :
        temp.append(A[j])
        j += 1
    i = p
    t = 0
    while i <= r:
        A[i] = temp[t]
        cnt += 1
        if cnt == K :
            result = A[i]
            break
        i += 1
        t += 1


merge_sort(nums, 0, N-1)
print(result)

