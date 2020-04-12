t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    profit = 0
    
    arr.sort()
    arr.reverse()
    
    for i in range(n):
        diff = arr[i] - i
        if diff >= 0:
            profit += diff
    
    print(profit%1000000007)
    
