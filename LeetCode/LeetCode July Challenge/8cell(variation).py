class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def prison(cells):
            temp = cells.copy()
            for j in range(1,len(cells)-1):
                if temp[j-1] ^ temp[j+1] == 0:
                    cells[j] = 1
                else:
                    cells[j] = 0
            cells[0],cells[-1] = 0,0
            return cells
        
        day1 = list(prison(cells))
        N -= 1
        count = 0
        
        while N > 0:
            day = list(prison(cells))
            N -= 1
            count += 1
            
            if day == day1:
                N = N%count
        return cells
