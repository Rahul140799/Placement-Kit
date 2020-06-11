def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        arr = []
        for i in range(len(coordinates)-1):
            try:
                slope = (coordinates[i][0]-coordinates[i+1][0])//(coordinates[i][1]-coordinates[i+1][1])
                arr.append(slope)
            except:
                slope = -999999999999999
                arr.append(slope)
        #print(arr)
        if len(set(arr)) == 1:
            return True
        else:
            return False
