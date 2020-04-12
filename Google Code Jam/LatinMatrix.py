t = int(input())
for i in range(t):
    n = int(input())
    
    mat = []
    s = 0
    
    for j in range(n):
        x = list(map(int,input().split()))
        mat.append(x)
        
    for a in range(n):
        s += mat[a][a]
        
    rc,cc = 0,0
    
    for a in range(n):
        row = []
        for b in range(n):
            if mat[a][b] not in row:
                row.append(mat[a][b])
        if len(row) != n:
            rc += 1
                
    for a in range(n):
        col = []
        for b in range(n):
            if mat[b][a] not in col:
                col.append(mat[b][a])
        if len(col) != n:
            cc += 1
                
    print("Case #"+str(i+1)+": "+str(s)+" "+str(rc)+" "+str(cc))
                
            
        
    
        
    
    
    
            
    
