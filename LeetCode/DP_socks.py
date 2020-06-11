def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        min_prices = 99999999999
        max_profit = 0
        
        for i in prices:
            min_prices = min(i,min_prices)
            max_profit = max(max_profit,i-min_prices)
        return max_profit
