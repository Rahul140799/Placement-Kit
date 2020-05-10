 def countElements(self, arr: List[int]) -> int:
        temp = []
        count = 0
        
        for i in arr:
            x = i+1
            temp.append(x)
        
        for i in temp:
            if i in arr:
                count += 1
        
        return count
    
