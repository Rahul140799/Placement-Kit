 def maxProfit(self, prices: List[int]) -> int:
        arr = []
        s = 0
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            arr.append(diff)
            
        for i in arr:
            if i > 0:
                s += i
        return s    
