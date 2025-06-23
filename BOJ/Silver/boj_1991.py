# [백준] 트리, 재귀 > 트리 순회

import sys
input = sys.stdin.readline

n = int(input())
tree = dict()
for _ in range(n) :
    root, left, right = input().strip().split()
    tree[root] = [left, right]

def func(x, order) :
    if order == "pre" :
        print(x, end="")
        for v in tree[x] :
            if v != '.' :
                func(v, order)
    elif order == "in" :
        if tree[x][0] != '.' :
            func(tree[x][0], order)
        print(x, end="")
        if tree[x][1] != '.' :
            func(tree[x][1], order)
    else :
        for v in tree[x] :
            if v != '.' :
                func(v, order)
        print(x, end="")

        
func('A', "pre")
print()
func('A', "in")
print()
func('A', "post")
print()