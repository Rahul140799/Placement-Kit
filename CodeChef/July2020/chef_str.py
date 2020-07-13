def guitar(arr):
    temp = []
    for i in range(len(arr)-1):
        temp.append(abs(arr[i] - arr[i+1])-1)
    return sum(temp)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    out = guitar(arr)
    print(out)
