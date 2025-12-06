# [백준] 트라이 > 전화번호 목록

class Node(object) :
    def __init__(self, key, data=None) :
        self.key = key
        self.data = data
        self.children = dict()

class Trie :
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
            else :
                return False
        return True

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    d = dict()
    n = int(input())
    phones = []
    for _ in range(n) :
        phones.append(input().strip())
    phones.sort(key = lambda x : len(x), reverse=True)
    for phone in phones :
        if phone[0] in d.keys() :
            if d[phone[0]].search(phone) : 
                print("NO")
                break
            else : d[phone[0]].insert(phone)
        else : 
            d[phone[0]] = Trie()
            d[phone[0]].insert(phone)
    else : print("YES")