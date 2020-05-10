def balancedStringSplit(self, s: str) -> int:
        r = 0
        l = 0
        cnt = 0
        flag = 1
        for i in s:
            if i == "R":
                r += 1
            if i == "L":
                l += 1
                
            if r == l:
                cnt += 1
                flag = 1
            else:
                flag = 0
        return cnt
