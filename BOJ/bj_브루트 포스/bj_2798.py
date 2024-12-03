# 백준 브루트 포스_1 : 블랙잭
[N, M] = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

nums.sort(reverse=True)
sums = []

def fun() :
    for a in range(0, N) :
        for b in range(1, N) :
            if a >= b : continue
            for c in range(2, N) :
                if b >= c : continue
                sum = nums[a] + nums[b] + nums[c]
                if sum <= M : 
                    sums.append(sum)
                else :
                    continue
        
fun()
print(max(sums))