    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        for i in range(2,len(nums)):
            nums[i] += max(nums[:i-1]) #Keeps track of the max value, leaving one house before it.
        return max(nums)

