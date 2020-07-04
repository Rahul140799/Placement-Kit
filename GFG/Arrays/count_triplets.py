def triplet(arr,n):
    arr.sort()
    maxi = arr[-1]
    count = 0
    d = {}
    
    for i in arr:
        d[i] = 1
        
    for i in range(n-1):
        for j in range(i+1,n-1):
            
            if arr[i]+arr[j] > maxi:
                break
            
            if arr[i]+arr[j] in d.keys():
                count += 1
                
    if count == 0:
        return -1
    else:
        return count

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    out = triplet(arr,n)
    print(out)
