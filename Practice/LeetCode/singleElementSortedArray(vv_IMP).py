def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        
        while(left<right):
            mid = (left + right)//2
            check_if_halves_are_even = (right-mid) % 2 == 0
            
            if nums[mid+1] == nums[mid]:        #if pair is on the right side and halves are even
                if check_if_halves_are_even:
                    left = mid+2
                else:                           #if pair is on the right side and halves are odd
                    right = mid-1
                    
            elif nums[mid-1] == nums[mid]:      #if pair is on the left side and halves are even
                if check_if_halves_are_even:
                    right = mid-2
                else:                           #if pair is on the left side and halves are odd
                    left = mid+1
                    
            else:                               #if element at mid is the culprit element, return 
                return nums[mid]
            
        return nums[left]                       #finally return the element,which is pointed by the left pointer
