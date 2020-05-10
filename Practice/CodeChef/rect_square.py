def square(l,b):
    if l < b:
        gcd = l
    else:
         gcd = b
    
    res = 0
    for i in range(1,gcd+1):
        if l%i == 0 and b%i ==0:
            res = i
    return res
    
t = int(input())
for i in range(t):
    l,b = map(int,input().split())
    out = square(l,b)
    print(out)

