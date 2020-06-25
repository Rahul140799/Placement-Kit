import math
def sieve_of_erasthonas(n2):
  temp = [i for i in range(2,n2)]
  for i in temp:
    if i > math.sqrt(n2):
      break
    if i != 0:
      for j in range(i*i,n2,i):
        temp[j-2] = 0
  return temp

def prime_check(arr):
  out = []
  for i in arr:
    if i > 1:
      for j in range(2,i):
        if i%j == 0:
          break
      else:
        out.append(i)
  return out
    
def fibonacci(mini,maxi,l):
  if l == 0:
    return mini
  elif l == 1:
    return maxi
  else:
    for i in range(2,l):
      c = mini+maxi
      mini = maxi
      maxi = c
    return maxi
    
def generate(n1,n2):
  li = sieve_of_erasthonas(n2)
  if n1 in li:
    ind = li.index(n1)
  else:
    for i in li:
      if i > n1:
        ind = li.index(i)
        break
  new_li = li[ind:].copy()
  x = filter(lambda a: a!=0 ,new_li)
  y = list(x)
  st = ""
  arr = []
  res = []
  for i in y:
    for j in y:
      st = str(i)+str(j)
      arr.append(int(st))
  final_prime = prime_check(arr)
  [res.append(x) for x in final_prime if x not in res]
  mini = min(res)
  maxi = max(res)
  l = len(res)
  fibo = fibonacci(mini,maxi,l)
  return fibo

t = int(input())
for _ in range(t):
  n1, n2 = map(int,input().split())
  out = generate(n1,n2)
  print(out)
