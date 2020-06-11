def findSecondMinimumValue(self, root: TreeNode) -> int:
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
        
        arr.sort()
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        if len(d) == 1:
            return -1
        
        count = 0
        for k in d.keys():
            if count == 1:
                return k
            else:
                count += 1
