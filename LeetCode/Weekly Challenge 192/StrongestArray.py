def getStrongest(self, arr: List[int], k: int) -> List[int]:
        res = []
        d = []

        if len(arr) == 1:
            return arr
        arr.sort()

        n = len(arr)
        mid = (len(arr)-1)//2
        med = arr[mid]
        
        for i in range(len(arr)):
            d.append([arr[i],abs(arr[i]-med)])
            
        x = sorted(d, key = lambda x:(-x[1],-x[0]))
        
        for i in range(k):
            res.append(x[i][0])
        return res
