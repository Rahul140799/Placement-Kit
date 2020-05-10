def backspaceCompare(self, S: str, T: str) -> bool:
        s =[]
        t =[]
        
        while S[0] == "#":
            S = S[1:]
        while T[0] == "#":
            T = T[1:]
            
        for i in S:
            if i != "#":
                s.append(i)
            elif i == "#" and len(s) > 0:
                s.pop()
                
        for i in T:
            if i != "#":
                t.append(i)
            elif i == "#" and len(t) > 0:
                t.pop()
                
            
        if s == t:
            return True
        else:
            return False
        
