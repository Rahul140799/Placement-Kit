def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        out = []
        for i,e in enumerate(groupSizes):
            #print("i:",i,"e:",e)
            d[e].append(i)
        #print(d)
        
        for length in d:
            while(len(d[length]) > 0):
                out.append(d[length][:length])
                d[length] = d[length][length:]
        return out
