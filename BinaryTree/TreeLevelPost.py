
class TreeNode:
    def __init__(self,left=None,right=None,value=0):
        self.left=left
        self.right=right
        self.value=value

root = [3,9,20,None,None,15,7]

root=TreeNode(value=3)
root.left=TreeNode(value=9)
root.right=TreeNode(value=20)
root.right.left=TreeNode(value=15)
root.right.right=TreeNode(value=7)




def treePost(root):

    if root is None:
        return 0

    left_depth=treePost(root.left)
    right_depth=treePost(root.right)

    return max(left_depth,right_depth)+1


print(treePost(root))