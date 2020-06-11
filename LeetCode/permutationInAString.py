    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = len(s1)
        y = len(s2)
        
        s1_counter = Counter(s1)
        window_counter = Counter()
        
        if x > y:
            return False
        
        for i,c in enumerate(s2):
            window_counter[c] += 1
            
            if i >= x:
                if window_counter[s2[i - x]] == 1:
                    del window_counter[s2[i-x]]
                else:
                    window_counter[s2[i-x]] -= 1
                    
            if window_counter == s1_counter:
                return True
        return False

