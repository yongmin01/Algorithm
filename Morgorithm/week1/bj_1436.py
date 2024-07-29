# 백준 브루트포스 알고리즘 : 영화감독 숌

movies = []
N = int(input())
num = 0
while (len(movies) < N) :
    num += 1
    if "666" in str(num) :
        movies.append(num)
print(movies[-1])