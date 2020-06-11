def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        self.dfs(image,sr,sc,oldColor,newColor)
        return image
    
    def dfs(self,image,sr,sc,oldColor,newColor):
        if sr<0 or sr>=len(image) or sc<0 or sc>=len(image[sr]) or image[sr][sc] != oldColor or image[sr][sc] == newColor:
            return 

        image[sr][sc] = newColor

        self.dfs(image,sr+1,sc,oldColor,newColor)
        self.dfs(image,sr-1,sc,oldColor,newColor)
        self.dfs(image,sr,sc+1,oldColor,newColor)
        self.dfs(image,sr,sc-1,oldColor,newColor)
        
        return self.dfs
