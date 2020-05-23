arr = list(map(int,input().split()))
days = int(input())
n = len(arr)
temp = [-1]*n

for i in range(days):
    temp[0] = 0^arr[1]
    temp[n-1] = 0^arr[n-2]
    for j in range(1,n-1):
        temp[j] = arr[j-1]^arr[j+1]
    for k in range(n):
        arr[k] = temp[k]
st = ""
for i in arr:
    st = st + str(i) + " "
print(st)
