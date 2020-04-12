t = int(input())
for z in range(t):
    s = input()
    
    cnt = 0
    l=[]
    arr=[]
    for i in s:
        l.append(int(i))
    
    if l[0]==0:
        arr.append(0)
    else:
        for i in range(l[0]):
            arr.append('(')
        cnt+=l[0]
        arr.append(l[0])
    
    for i in range(1,len(l)):
        diff = l[i]-l[i-1] 
        if diff<0:
            for k in range(abs(diff)):
                arr.append(')')
            cnt+=diff
            arr.append(l[i])
        elif diff>0:
            for k in range(abs(diff)):
                arr.append('(')
            cnt+=diff
            arr.append(l[i])
        else:
            arr.append(l[i])
    for i in range(cnt):
        arr.append(')')
    st=""
    for i in arr:
        st+=str(i)
    print("Case #"+str(z+1)+": "+st)
            
            
            
            
            
            
            
