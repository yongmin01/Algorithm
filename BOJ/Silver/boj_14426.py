# [백준] 이분 탐색, 트라이 > 접두사 찾기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
S = []
for _ in range(n) :
    S.append(input().strip())
S.sort()

def di(word, start, end) :
    while start <= end :
        mid = (start + end) // 2
        if word in S[mid] : 
            for i in range(len(word)) :
                if word[i] != S[mid][i] : break
            else : 
                return True
        if word < S[mid] :
            end = mid -1
        else : start = mid + 1
    return False

answer = 0 
for _ in range(m) :
    word = input().strip()
    if di(word, 0, n-1) :
        answer += 1
    
print(answer)

# Trie 자료구조 사용한 풀이 #
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

class Node (object) :
    def __init__(self, key, data=None) :
        self.key = key
        self.data = data
        self.children = {}

class Trie (object) :
    def __init__(self) :
        self.head = Node(None)
    
    def insert(self, string) :
        curr_node = self.head
        for char in string :
            if char not in curr_node.children :
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        
        curr_node.data = string
    
    def search(self, string) :
        curr_node = self.head
        for char in string :
            if char in curr_node.children :
                curr_node = curr_node.children[char]
            else : return False
        
        
        return True
    
trie = Trie()
for _ in range(n) :
    trie.insert(input().strip())

answer = 0
for _ in range(m) :
    if trie.search(input().strip()) : 
        answer += 1

print(answer)