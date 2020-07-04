# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return
        
        arr = []
        queue = []
        queue.append(root)
        
        while(len(queue) > 0):
             
            print(queue)
            print(len(queue))
            
            size = len(queue)
            currentLevel = []
            for i in range(size):
                current = queue.pop(0)
                print("Pop",current.val)
                currentLevel.append(current.val)
            
                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)
            arr.append(currentLevel)
        return arr[::-1]
