def countSquares(self, matrix: List[List[int]]) -> int:
        m  = len(matrix)
        n = len(matrix[0])
        count = 0
        res = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == 1:
                    res[i][j] = 1 + min(res[i-1][j],res[i-1][j-1],res[i][j-1])
                    count += res[i][j]
        return count
