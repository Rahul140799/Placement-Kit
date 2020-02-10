l = int(input())
for i in range(0,l):
    n = int(input())
    list = []
    
    for i in range(0,n):
        x = int(input())
        list.append(x) 
    
    max = list[0]
    max_Index = 0
    
    for i in range (0,len(list)):
        if list[i] > max: 
                
            max_Index = i;
            max = list[i];
        
    print(max_Index+max);
