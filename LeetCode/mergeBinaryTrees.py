class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None and t2 == None:
            return None
        if t1 == None and t2 != None:
            return t2
        if t2 == None and t1 != None:
            return t1
        
        res = TreeNode(t1.val+t2.val)
        res.left = self.mergeTrees(t1.left,t2.left)
        res.right = self.mergeTrees(t1.right,t2.right)
        
        return res
