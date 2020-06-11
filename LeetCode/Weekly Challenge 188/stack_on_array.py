def buildArray(self, target: List[int], n: int) -> List[str]:
        arr = []
        
        for i in range(1,n+1):
            if i in target:
                arr.append("Push")
            else:
                arr.append("Push")
                arr.append("Pop")
                
            if i == target[len(target)-1]:
                break
        return arr
