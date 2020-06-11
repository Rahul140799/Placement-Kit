t = int(input())
for i in range(0,t):
    n,k = map(int,input().split())
    sum = 0
    
    arr = list(map(int,input().split()))
    
    for i in range(0,n):
        sum = sum + arr[i]
    rem = sum % k 
    print(rem)
    