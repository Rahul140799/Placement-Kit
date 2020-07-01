def arrangeCoins(self, n: int) -> int:
	
	#Solution1        
	if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(1,n+1):
            n -= i
            if n < 0:
                break
            else:
                continue
        return i-1

        #Solution2
        if n<2:
            return n
        
        for i in range(1,n+1):
            if i*(i+1)//2 > n:
                return i-1
            else:
                continue
