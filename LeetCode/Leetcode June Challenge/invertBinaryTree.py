def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        
	//DFS the left first and then right
        left = self.invertTree(root.left)    ---------
     ---right = self.invertTree(root.right)	     |	
     |   					     | Transfer of control   	
     |   root.right = left <--------------------------
     |-->root.left = right
        
        return root 

Note: Root is set at left everytime in first traversal & and resp. left and right are swapped	
      Root is set at right everytime in second traversal & and resp. left and right are swapped
     
