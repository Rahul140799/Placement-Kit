import heapq 
def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq.heapify(stones)
        
        if len(stones) == 1:
            return stones[0]
        
        if len(stones) == 2:
            return abs(stones[0]-stones[1])
        
        for i in range(len(stones)-1):
            x = heapq.nlargest(2,stones)
            y = x[0]-x[1]
            stones.remove(x[0])
            stones.remove(x[1])
            heapq.heappush(stones,y)
            
        return stones[0]
