class Node:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.lef=left
        self.right=right


def dfs(root):
    if root is None:
        return
    dfs(root.left)
    dfs(root.right)

