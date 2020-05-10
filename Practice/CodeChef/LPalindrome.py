def lpal(st):
    d1 = {}
    d2 = {}
    
    l = len(st)
    h = l//2
    
    if l < 2:
        print("NO")
    
    if l%2 == 0:
        for i in range(h):
            if st[i] not in d1:
                d1[st[i]] = 1
            else:
                d1[st[i]] += 1
        
        for j in range(h,l):
            if st[j] not in d2:
                d2[st[j]] = 1
            else:
                d2[st[j]] += 1
    else:
        for i in range(h):
            if st[i] not in d1:
                d1[st[i]] = 1
            else:
                d1[st[i]] += 1
        
        for j in range(h+1,l):
            if st[j] not in d2:
                d2[st[j]] = 1
            else:
                d2[st[j]] += 1
    
    if d1 == d2:
        print("YES")
    else:
        print("NO")
        
t = int(input())
for _ in range(t):
    st = input()
    out = lpal(st)

