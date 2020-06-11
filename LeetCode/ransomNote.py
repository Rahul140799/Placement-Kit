 def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        r = {}
        flag = 0
        
        if len(ransomNote) == 0:
            return True
        if len(magazine) == 0:
            return False
        
        for i in magazine:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
                
        for i in ransomNote:
            if i not in r:
                r[i] = 1
            else:
                r[i] += 1

        #print("Mag:",m)
        #print("Ran:",r)
        
        for k,v in r.items():
            if k in m.keys() and v <= m[k]:
                #print("k:",k," ","v:",v,m[k])
                flag = 1
            else:
                return False 
                
        if flag == 1:
            return True
