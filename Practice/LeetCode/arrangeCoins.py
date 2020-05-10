def arrangeCoins(self, n: int) -> int:
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
