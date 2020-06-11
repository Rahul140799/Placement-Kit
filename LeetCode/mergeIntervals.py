def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x:x[0])
        
        if len(intervals) <= 1:
            return intervals
        
        i = 0
        
        while(i<len(intervals)):
            a = intervals[i][0]
            b = intervals[i][1]
            while((i+1) < len(intervals) and intervals[i+1][0]<=b):
                b = max(b,intervals[i+1][1])
                i += 1
            res.append([a,b])
            i+=1
        return res
