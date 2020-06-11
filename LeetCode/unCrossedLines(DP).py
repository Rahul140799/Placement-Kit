    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        l1 = len(A)
        l2 = len(B)
        
        arr = [ [0 for i in range(l2+1)] for j in range(l1+1)]
        
        for i in range(l1):
            for j in range(l2):
                if A[i] == B[j]:
                    arr[i+1][j+1] = arr[i][j] + 1
                else:
                    arr[i+1][j+1] = max(arr[i+1][j],arr[i][j+1])
                    
        return arr[-1][-1]

