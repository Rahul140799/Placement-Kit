class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = []
        self.point = 0
        self.arr.insert(self.point,homepage)

    def visit(self, url: str) -> None:
        self.point += 1
        self.arr.insert(self.point,url)
        
        for i in range(self.point+1,len(self.arr)):
            self.arr.pop()
        
    def back(self, steps: int) -> str:
        for i in range(steps):
            self.point -= 1
            if self.point < 0:
                self.point = 0
                break
        return self.arr[self.point]
        
    def forward(self, steps: int) -> str:
        if steps+self.point >= len(self.arr)-1:
            self.point = len(self.arr)-1
        else:
            self.point += steps
        return self.arr[self.point]

