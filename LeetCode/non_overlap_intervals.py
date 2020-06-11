def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        safe = 0
        prev = -9999999999999999999
        intervals.sort(key = lambda x:x[1]) #sorting by order of end time so that any (i+1) start time                                             #less than (i)th end time can be removed.
        
        #print(intervals)
        
        for i in intervals:
            if i[0] >= prev:
                #print("For:",i)
                #print("i[0]:",i[0]," ","prev:",prev)
                prev = i[1]
                #print("res:",prev)
            else:
                safe += 1
                #print("Failing",safe)
            #print("")
        return safe
