def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        s = 0
        max_len = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        #Idea is to make 0 as -1 and whenever sum is 0, consider it as an contiguous subarray
        for i in range(len(nums)):
            s += nums[i]
            if s == 0:
                max_len = i+1
            
            if s in d:
                if max_len < i - d[s]:
                    max_len = i - d[s]
            else:
                d[s] = i
                    
        return max_len
