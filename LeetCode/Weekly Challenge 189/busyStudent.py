def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        l = len(startTime)
        count = 0
        
        if l == 1:
            if startTime[0] < queryTime and endTime[0] < queryTime:
                return 0
            elif startTime[0] <= queryTime and endTime[0] >= queryTime:
                return 1
            else:
                return 0
        
        for i in range(l):
            for j in range(startTime[i],endTime[i]+1):
                if queryTime == j:
                    count += 1
        return count
