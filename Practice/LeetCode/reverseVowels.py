def reverseVowels(self, s: str) -> str:
        
        start = 0
        end = len(s)
        arr = ['a','e','i','o','u','A','E','I','O','U']
        c = list(s)
        
        if len(s) == 1:
            return s
        
        while(start < end):
            if c[start] in arr:
                end -= 1
                if c[end] in arr:
                    temp = c[start]
                    c[start] = c[end]
                    c[end] = temp
                    start += 1
                else:
                    continue
            else:
                start += 1
                
        st = ""
        for i in c:
            st += i
        return st
