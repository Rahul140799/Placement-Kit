def checkValidString(self, s: str) -> bool:
        leftCount = 0
        rightCount = 0
        
        if len(s) == 0:
            return True
        
        if len(s) == 1 and s != "*":
            return False
        elif len(s) == 1 and s == "*":
            return True
        
        for i in s:
            if i == ")":
                leftCount -= 1
            else:
                leftCount += 1
                
            if leftCount < 0:
                return False
        
        if leftCount == 0:
            return True
        
        for i in reversed(s):
            if i == "(":
                rightCount -= 1
            else:
                rightCount += 1
            
            if rightCount < 0:
                return False
            
        return True
