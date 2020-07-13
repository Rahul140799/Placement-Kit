d1 = {}
d2 = {}

def rect(x,y):
    global d1
    global d2
    
    if x not in d1:
        d1[x] = 1
    else:
        d1[x] += 1
    
    if y not in d2:
        d2[y] = 1
    else:
        d2[y] += 1

    return d1,d2

def dic(d1,d2):
  for k,v in d1.items():
        if v%2 != 0:
            res1 = k
            break
    
  for k,v in d2.items():
      if v%2 != 0:
          res2 = k
          break
  return res1,res2

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range((4*n)-1):
        x,y = map(int,input().split())
        c1,c2 = rect(x,y)

    res1,res2 = dic(c1,c2)
    print(res1,res2)
    
    d1 = {}
    d2 = {}

