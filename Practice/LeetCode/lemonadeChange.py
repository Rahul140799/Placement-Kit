def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5:0,10:0,20:0}
        
        for i in bills:
            d[i] += 1
            
            i -= 5
            
            if i == 0:
                continue
            
            elif i == 5:
                if d[5]:
                    d[5] -= 1
                else:
                    return False
            elif i == 15:
                if d[10] and d[5]:
                    d[10] -= 1
                    d[5] -= 1
                elif d[5] >= 3:
                    d[5] -= 3 
                else:
                    return False
        
        return True
