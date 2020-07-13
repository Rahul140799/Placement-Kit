def chefina(a,b):
    a.sort()
    b.sort()
    
    d1 = {}
    d2 = {}
    d3 = {}
    
    count = 0
    
    if a == b:
        return 0
    
    for i in a:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1
    
    for i in b:
        if i not in d2:
            d2[i] = 1
        else:
            d2[i] += 1
    
    temp = a+b #merging both lists
    
    for i in temp:
        if i not in d3:
            d3[i] = 1
        else:
            d3[i] += 1
    
    for k,v in d3.items():
        if v%2 != 0:
            return -1
    
    swap_a = []
    swap_b = []
    
    for k,v in d1.items():
        if v > d3[k]//2:
            swap_a.extend([k]*(v - d3[k]//2))
    
    for k,v in d2.items():
        if v > d3[k]//2:
            swap_b.extend([k]*(v - d3[k]//2))
    
    swap_a.sort()
    swap_b.sort(reverse = True)
    
    cost = 0
    temp.sort()
    
    for i in range(len(swap_a)):
        cost += min(2*temp[0], min(swap_a[i],swap_b[i]))
    return cost

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    out = chefina(a,b)
    print(out)

