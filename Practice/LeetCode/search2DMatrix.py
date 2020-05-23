def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for myList in matrix:				#For every list in 2D list
            if self.binarySearch(myList,target):	#Do Binary Search
                return True
        return False
    
    def binarySearch(self,myList,target):		#Binary Search Logic
        left = 0
        right = len(myList)-1
        
        while(left <= right):                     
            mid = int(left+(right-left)/2)
            if myList[mid] == target:
                return True
            elif myList[mid] > target:
                right = mid-1
            elif myList[mid] < target:
                left = mid+1
        return False
