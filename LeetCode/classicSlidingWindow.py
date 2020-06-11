def hasAllCodes(self, s: str, k: int) -> bool:
        arr = set()
        i = 0
        x = int( ('1'*k) )
        while(i < len(s)-k+1):
            new = int(s[i:i+k])
            out = new ^ x
            arr.add(out)
            i += 1
        if len(arr) == 2**k:
            return True
        else:
            return False
