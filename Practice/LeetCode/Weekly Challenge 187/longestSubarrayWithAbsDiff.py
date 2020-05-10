def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        mini = 9999999999999
        maxi = -9999999999999
        
        left = 0
        right = 0
        windowSize = 0
        l = len(nums)
        
        while(left < l and right < l):
            mini = min(mini,nums[right])
            maxi = max(maxi,nums[right])
            
            if maxi-mini > limit:
                left += 1
                mini = 9999999999999
                maxi = -9999999999999                
                for i in range(left,right):
                    mini = min(mini,nums[i])
                    maxi = max(maxi,nums[i])
            
            else:
                windowSize = max(right-left+1,windowSize)
                right += 1
                
        return windowSize
