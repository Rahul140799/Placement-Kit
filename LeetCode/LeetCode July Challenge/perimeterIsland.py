def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def dfs(r,c):
            if r<0 or r>len(grid)-1 or c<0 or c>len(grid[0])-1:
                return 0
            return grid[r][c]
        
        peri = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cont = 4
                if grid[i][j] == 1:
                    cont -= (dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1))
                    peri += cont
        return peri
