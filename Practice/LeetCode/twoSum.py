def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(nums)
        d = {}
        while(i<j):
            rem = target-nums[i]
            if rem in d:
                return d[rem],i
            else:
                d[nums[i]] = i
                i += 1
