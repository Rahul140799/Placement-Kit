def validMountainArray(self, A: List[int]) -> bool:
        if len(A) == 0:
            return False
        
        maxi = max(A)
        ind = A.index(maxi)
        flag = 0
        
        if ind == 0 or ind==len(A)-1:
            return False
        
        if len(A) == 3 and A[ind] > A[ind-1] and A[ind] > A[ind+1]:
            return True
        
        for i in range(ind-1):
            if A[i] < A[i+1]:
                flag = 1
            else:
                return False
            
        for i in range(ind+1,len(A)-1):
            if A[i] > A[i+1]:
                flag = 1
            else:
                return False
