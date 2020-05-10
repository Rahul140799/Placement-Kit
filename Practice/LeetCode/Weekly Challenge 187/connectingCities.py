class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        arr = []
        for i in range(len(paths)):
            for j in range(len(paths[i])):
                #print(paths[i][j])
                
                if paths[i][0] not in d:
                    d[paths[i][0]] = paths[i][1] 
        
        for k,v in d.items():
            if v not in d.keys():
                return v
                    
