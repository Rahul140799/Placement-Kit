def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
        arr = nums.copy()
        arr.sort()
        
        for i in range(len(arr)-2):
            if(i==0 or (i>0 and arr[i] != arr[i-1])):
                j = i+1
                k = len(arr)-1
                while(j<k):
                    if arr[i] + arr[j] + arr[k] == 0:
                        res.append([arr[i],arr[j],arr[k]])
                        while(j<k and arr[j] == arr[j+1]):
                            j += 1
                        while(j<k and arr[k] == arr[k-1]):
                            k -= 1
                        
                        j += 1
                        k -= 1
                    elif arr[i]+arr[j]+arr[k] > 0:
                        k -= 1
                    else:
                        j += 1
        return res
