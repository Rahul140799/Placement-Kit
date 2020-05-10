def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
            
        res = []
        for i in range(len(nums)):
            x = left[i] * right[i]
            res.append(x)
        return res

(Brilliant) Logic : 

	1 2 3 4
	
left 	1 1 	 	1 	1 (initially)
	  ^(start)
now  	  1(1*1) 	2(1*2) 6(2*3)

right 	1         1 	        1		1 (initially)
		  ^(start here)  
  	24(12*2)  12(4*3)       4(4*1)
