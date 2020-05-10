def prms(n):
    arr = []
    out = []
    fact = 1
        
    if n == 1:
        return "NO"
        
    for i in range(2,n):
        fact = fact*(i-1)
        if (fact+1)%i == 0:
            arr.append(i)
    
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]*arr[j] <= n:
                out.append(arr[i]*arr[j])
    
    out.sort()
    
    start = 0
    end = len(out)-1
    while(start<end):
        req = n-out[start]
        if req in out:
            return "YES"
        else:
            start += 1
    return "NO"
    
t = int(input())
for _ in range(t):
    n = int(input())
    out = prms(n)
    print(out)
