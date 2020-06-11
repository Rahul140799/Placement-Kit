def priceon(arr,k):
    curr = sum(arr)
    new = 0
    temp = []
    for i in arr:
        if i > k:
            temp.append(k)
        else:
            temp.append(i)
    new = sum(temp)
    return curr - new
    

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    out = priceon(arr,k)
    print(out)
