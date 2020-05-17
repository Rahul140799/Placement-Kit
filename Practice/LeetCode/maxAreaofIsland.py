def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res = max(res,self.dfs(grid,i,j,count))
        return res
    
    def dfs(self,grid,i,j,count):
        c = count
        if i>=0 and i<len(grid) and j>=0 and j<len(grid[i]) and grid[i][j] == 1:      
            grid[i][j] = -1
            c += 1
            c = self.dfs(grid,i+1,j,c)
            c = self.dfs(grid,i-1,j,c)
            c = self.dfs(grid,i,j+1,c)
            c = self.dfs(grid,i,j-1,c)

        return c
        
