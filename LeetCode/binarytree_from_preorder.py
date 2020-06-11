# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = sorted(preorder)
        return self.preInOrder(preorder,inorder)
        
    def preInOrder(self,preorder,inorder):
        if len(inorder) != len(preorder) or preorder == None or inorder == None or len(preorder) == 0 or len(inorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        ind  = inorder.index(root.val)
        
        root.left = self.preInOrder(preorder[1:ind+1],inorder[:ind])
        root.right = self.preInOrder(preorder[ind+1:],inorder[ind+1:])
        
        return root
