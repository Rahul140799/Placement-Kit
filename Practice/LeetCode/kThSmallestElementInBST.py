 def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root == None:
            return
        arr = []
        def inorder(root):
            if root == None:
                return 
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        
        if len(arr) == k:
            return arr[len(arr)-1]
        else:
            for i in range(len(arr)-1):
                if (i+1) == k:
                    return arr[i]
