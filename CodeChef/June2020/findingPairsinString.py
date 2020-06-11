def xystr(s):
    pCount = 0
    count = 0
    flag = s[0]
    
    for i in range(len(s)):
        if s[i] == flag:
            pCount = count
        else:
            if(count - pCount)==0:
                pCount = count
                count += 1
                flag = s[i]
            else:
                pCount = count
                flag = s[i]
    return count

t = int(input())
for _ in range(t):
    s = input()
    out = xystr(s)
    print(out)

