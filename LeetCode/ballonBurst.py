def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        end = -9999999999999999999999999
        count = 0
        for i in points:
            if i[0] <= end:
                count += 1
            else:
                end = i[1]
        return len(points)-count
