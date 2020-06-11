 def isSubsequence(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen = len(t) 

        i = 0    
        j = 0    

        while i<slen and j<tlen:
            print("s[i]:",s[i])
            print("t[j]:",t[j])
            if s[i] == t[j]:
                i += 1
                print("i:",i)
            j += 1
            print("j:",j)

        return i==slen
            
