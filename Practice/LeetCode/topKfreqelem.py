def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        count = 0
        arr = []
        
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
        x = {k:v for k,v in sorted(d.items(), key=lambda item:item[1],reverse = True)}
        
        for i in x.keys():
            if count < k:
                arr.append(i)
                count += 1
            else:
                break
        return arr
