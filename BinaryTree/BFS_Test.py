from collections import deque


class Node:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.lef=left
        self.right=right

def bfs(root):
    visited=[]
    if root is None:
        return 0

    q=deque()
    q.append(root)

    while q:
        cur_node=q.popleft()
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)

        if cur_node.right:
            q.append(cur_node.right)

    return visited