def findAnagrams(self, s: str, p: str) -> List[int]:
        slen = len(s)
        plen = len(p)
        
        s_counter = Counter()
        p_counter = Counter(p)
        
        res = []
        
        for i in range(slen):
            s_counter[s[i]] += 1
            if(i>=plen):
                if s_counter[s[i - plen]] == 1:
                    del s_counter[s[i - plen]]
                else:
                    s_counter[s[i - plen]] -= 1
            
            if s_counter == p_counter:
                res.append(i-plen + 1)
        return res
