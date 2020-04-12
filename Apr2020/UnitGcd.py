def unitgcd(n):
    arr = []
    x = []
    new = []
  
    for i in range(1,n+1):
        arr.append(i)
    if n%2!=0:
        for i in arr:
            if i < 4:
                x.append(i)
        new.append(x)
        if n>3:
            for i in range(3,n,2):
                x=[]
                x.append(i+1)
                x.append(i+2)
                new.append(x)
  
    elif n%2 == 0:
        for i in arr:
            if i < 3:
                x.append(i)
        new.append(x)
        if n > 2:
            for i in range(2,n,2):
                x = []
                x.append(i+1)
                x.append(i+2)
                new.append(x)
    return new
  
if __name__ == "__main__":        
    t = int(input())
    for i in range(t):
        n = int(input())
        new = unitgcd(n)
        print(len(new))
        for i in new:
            print(len(i),end=" ")
            for j in range(len(i)):
                if j is not len(i)-1:
                    print(i[j],end=" ")
                else:
                    print(i[j])

