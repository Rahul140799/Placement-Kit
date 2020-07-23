def jumpman(n,nums):
    if n <= 1:
        return 1
    
    last = n-1
    for i in range(n-1,-1,-1):
        if i+nums[i] >= last:
            last = i
    
    if last == 0:
        return 1
    else:
        return 0

n = int(input())
arr = list(map(int,input().split()))
out = jumpman(n,arr)
print(out)
