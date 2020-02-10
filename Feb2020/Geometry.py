t = int(input())
for i in range(0,t):
    n = int(input())
    x = []
    y = []
    sum = 0
    
    x = list(map(int, input().split()))
    x.sort()
        
    y = list(map(int,input().split()))
    y.sort()
        
    for i in range(0,n):
        sum = sum + min(x[i],y[i])
    print(sum)
    
    x = []
    y = []