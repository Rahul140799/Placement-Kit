def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root == None:
            return 0
        s = 0
        if root.val %2 == 0:
            x = 0
            y = 0
            if root.left:
                if root.left.left:
                    x = root.left.left.val
                else:
                    x = 0
                if root.left.right:
                    y = root.left.right.val
                else:
                    y = 0
            s += x + y
            
            a = 0
            b = 0
            if root.right:
                if root.right.left:
                    a = root.right.left.val
                else:
                    a = 0
                if root.right.right:
                    b = root.right.right.val
                else:
                    b = 0
            s += a + b
        return s + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)
