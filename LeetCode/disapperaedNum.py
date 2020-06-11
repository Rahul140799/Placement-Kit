( O(1)time & no additional space )
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        out = []
        for i in nums:
            if nums[abs(i)-1] > 0:
                nums[abs(i)-1] = -nums[abs(i)-1]
        for i in range(len(nums)):
            if nums[i] > 0:
                out.append(i+1)
        return out
