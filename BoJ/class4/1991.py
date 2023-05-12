import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

n=int(input())
tree={}

for i in range(n):
    root,left,right=map(str, input().split())
    tree[root]=[left,right]

def preorder(root):
    if root != '.':
        print(root,end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        preorder(tree[root][0])
        print(root,end='')
        preorder(tree[root][1])

def postorder(root):
    if root != '.':
        preorder(tree[root][0])
        preorder(tree[root][1])
        print(root,end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')

