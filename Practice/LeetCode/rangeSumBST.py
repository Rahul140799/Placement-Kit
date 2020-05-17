class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        arr=[]
        def inOrder(root):
            if root:
                inOrder(root.left)
                arr.append(root.val)
                inOrder(root.right)
        inOrder(root)
        i = arr.index(L)
        j = arr.index(R)
        s = 0
        for k in range(i,j+1):
            s += arr[k]
        return s
