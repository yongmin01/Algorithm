N = int(input())
y = 0
while y < N :
    print((" " * (N-y-1)) + ("*" * (2 * y + 1)))
    y += 1
y -= 2
while y >= 0 :
    print((" " * (N - y - 1)) + ("*" * (2 * y + 1)))
    y -= 1