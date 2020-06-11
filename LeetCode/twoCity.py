def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        s = 0
        a = 0
        b = 0
        n = len(costs)
        #diff = []
        costs.sort(key = lambda x:abs(x[0]-x[1]))
        
        for i in costs[::-1]:
            if a < n//2 and b < n//2:
                s += min(i)
                #diff.append(min(i))
                ind = i.index(min(i))
                if ind == 0:
                    a += 1
                else:
                    b += 1
            elif b >= n//2:
                s += i[0]
                #diff.append(i[0])
                a += 1
            else:
                s += i[1]
                b += 1
        #print(diff)
        return s
