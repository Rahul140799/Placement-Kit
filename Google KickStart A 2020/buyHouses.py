def buy(arr,b):
    count = 0
    cost = 0
    arr.sort()
    for i in range(len(arr)):
        cost += arr[i]
        if cost <= b:
            count += 1
        else:
            break
    return count

t = int(input())
for k in range(t):
    n,b = map(int,input().split())
    arr = list(map(int,input().split()))
    out = buy(arr,b)
    print("Case #"+str(k+1)+":",out)
    
