def search(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums)
        
        while(start<end):
            mid = (start+end-1)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                end = mid
            else:
                start = mid+1
        return -1
