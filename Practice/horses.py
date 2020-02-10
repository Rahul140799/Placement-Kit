t = int(input())

for i in range(0,t):
    
    x = int(input())
    
    skill=[int(x)for x in input().split(" ")]
    
    list_1 = [] 
    list_1 = sorted(skill)
  
    list_2 = []
    
    for i in range(0,len(list_1)-1):
        diff = list_1[i+1] - list_1[i]
        list_2.append(diff)
        
    print(min(list_2))
    