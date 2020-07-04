def nthUglyNumber(self, n: int) -> int:
        ugly = [0]*n
        
        ugly[0] = 1
        
        i2,i3,i5 = 0,0,0
        
        two = 2
        three = 3
        five = 5
        
        for i in range(1,n):
            ugly[i] = min(two,three,five)
            
            if ugly[i] == two:
                i2 += 1
                two = ugly[i2]*2
                
            if ugly[i] == three:
                i3 += 1
                three = ugly[i3]*3
            
            if ugly[i] == five:
                i5 += 1
                five = ugly[i5]*5
        
        return ugly[-1]
                
