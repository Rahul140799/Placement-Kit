def transpose(self, A: List[List[int]]) -> List[List[int]]:
        res = [[0]*len(A) for _ in range(len(A[0])) ]
        for r in range(len(A[0])):
            for c in range(len(A)):
                res[r][c] = A[c][r]
        return res
