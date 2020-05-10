def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        x = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse = True)}
        
        st = ""
        for i in x:
            st += i*x[i]
        return st
