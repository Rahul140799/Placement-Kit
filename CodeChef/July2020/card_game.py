count1 = 0
count2 = 0

def cards(a,b):
    s1 = 0
    s2 = 0
    global count1
    global count2
    
    while(a>0):
        s1 += int(a%10)
        a = int(a/10)
    while(b>0):
        s2 += int(b%10)
        b = int(b/10)
    
    if s1>s2:
        count1 += 1
    elif s1 == s2:
        count1 += 1
        count2 += 1
    else:
        count2 += 1
    return count1,count2

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        a,b = map(int,input().split())
        c1,c2 = cards(a,b)

    if c1 > c2:
        print(0,c1)
    elif c1 == c2:
        print(2,c1)
    else:
        print(1,c2)
    
    count1 = 0
    count2 = 0 


