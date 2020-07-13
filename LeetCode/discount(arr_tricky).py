def finalPrices(self, prices: List[int]) -> List[int]:
        ind = 0
        found = False
        
        for i in range(len(prices)):
            found = False
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    ind = j
                    found = True
                    break
            
            if found:
                prices[i] -= prices[ind]
                
        return prices
