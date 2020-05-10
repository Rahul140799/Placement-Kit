def stringShift(self, s: str, shift: List[List[int]]) -> str:
        count = 0
        s1 = list(s)
        st = ""
        for i in shift:
            if i[0] == 0:
                count += i[1]
            elif i[0] == 1:
                count -= i[1]
        
        if count < 0:
            for i in range(abs(count)):
                x = s1.pop(index(len(s)-1))
                s1.insert(0,x)
            for i in s1:
                st += i
            return st
    
        elif count > 0:
            for i in range(count):
                y = s1.pop(index(0))
                s1.append(y)
            for i in s1:
                st += i
            return st
    
        elif count == 0:
            return s
