t = int(input())
for z in range(t):
    n = int(input())
    arr=[]
    for i in range(n):
        x = list(map(int,input().split()))
        arr.append(x)
    res=[]
    c=[]
    j=[]
    minc,maxc,minj,maxj,flag=0,0,0,0,0
    
    for i in range(n):
        if (arr[i][0]<=minc and arr[i][1]<=minc) or (arr[i][0]>=maxc and arr[i][1]>=maxc) or (arr[i][0] in c and arr[i][1] in c):
            res.append('C')
            c.append(arr[i][0])
            c.append(arr[i][1])
            minc = min(c)
            maxc = max(c)
        
        elif (arr[i][0]<=minj and arr[i][1]<=minj) or (arr[i][0]>=maxj and arr[i][1]>=maxj) or (arr[i][0] in j and arr[i][1] in j):
            res.append('J')
            j.append(arr[i][0])
            j.append(arr[i][1])
            minj = min(j)
            maxj = max(j)
        else:
            flag=1
            break
    
    if flag==1:
        print("Case #"+str(z+1)+": "+"IMPOSSIBLE")
    elif flag==0:
        st = ""
        for i in res:
            st+=str(i)
        print("Case #"+str(z+1)+": "+st)
        
        
