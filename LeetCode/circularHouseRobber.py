def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        dp1 = nums.copy()
        dp2 = nums[::-1].copy()         #Rob last house, but not first time ; hence reversing
        
        for i in range(2,len(nums)-1):
            dp1[i] += max(dp1[:i-1])    #basic house robber
            dp2[i] += max(dp2[:i-1])
        
        x = max(dp1)
        y = max(dp2)
        
        return max(x,y)
