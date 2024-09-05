# 백준_트리 & 재귀 : 이진 검색 트리

import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

nums = []
while True :
    num = input()
    if num == '' :
        break
    else :
        nums.append(int(num))

class Node:
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self, root) :
        self.root = root

    def insert(self, value) :
        self.currentNode = self.root
        while True :
            if value < self.currentNode.value :
                if self.currentNode.left != None :
                    self.currentNode = self.currentNode.left
                else :
                    self.currentNode.left = Node(value)
                    break
            elif value > self.currentNode.value :
                if self.currentNode.right != None :
                    self.currentNode = self.currentNode.right
                else :
                    self.currentNode.right = Node(value)
                    break


root = Node(nums[0])
tree = BinarySearchTree(root)

for i in range(1, len(nums)) :
    tree.insert(nums[i])

def post_order(root) :
    if root == None :
        return
    else :
        post_order(root.left)
        post_order(root.right)
        print(root.value)
    
post_order(tree.root)