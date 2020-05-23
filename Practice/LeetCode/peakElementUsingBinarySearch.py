def peakIndexInMountainArray(self, A: List[int]) -> int:
        start = 0
        end = len(A)-1
        
        while(start<end):
            mid = (start+end)//2
            
            if((A[mid] > A[mid-1]) and (A[mid] > A[mid+1])):
                return mid
            elif((A[mid] > A[mid-1]) and (A[mid+1] > A[mid])):
                start = mid+1
            else:
                end = mid
