def slider(arr,s):
    cs = arr[0]
    start = 0
    i = 1
    n = len(arr)
    while(i<=n):
        while(cs > s and start < i-1):
            cs = cs - arr[start]
            start += 1
        if cs == s:
            print(start+1,i)
            return 1
        if i < n:
            cs += arr[i]
        i += 1
    print("-1")
    return 0

t = int(input())
for _ in range(t):
    n,s = map(int,input().split())
    arr = list(map(int,input().split()))
    slider(arr,s)
