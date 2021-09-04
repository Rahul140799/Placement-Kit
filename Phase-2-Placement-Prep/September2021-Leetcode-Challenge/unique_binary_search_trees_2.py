# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

# Example 1:
#     Input: n = 3
#     Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

# Example 2:
#     Input: n = 1
#     Output: [[1]]

# Constraints:

# 1 <= n <= 8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        if n == 0:
            return []
        
        def recurse(left, right):
            res = []
            if left > right:
                res.append(None)
                return res
            
            for i in range(left, right+1):
                temp_left = recurse(left, i-1)
                temp_right = recurse(i+1, right)
                for l in temp_left:
                    for r in temp_right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res
        
        return recurse(1,n)

#TC : O(2^n)
#SC : O(2^n)