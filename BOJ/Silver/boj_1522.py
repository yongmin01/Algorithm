# [백준] 브루트포스, 슬라이딩 윈도우 > 문자열 교환

string = input().strip()
window_size = string.count('b')
string_len = len(string)

count = string[:window_size].count('b')
temp = count

for i in range(1, string_len) :
    if string[i-1] == 'b' : temp -= 1
    if string[(i+window_size-1)%string_len] == 'b' : temp += 1
    count = max(count, temp)
    
print(window_size-count)