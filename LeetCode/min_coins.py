def min_coin(n):
  for i in range(1,n):
    if i*(i+1) >= 2*n:
      return i

t = int(input())
for _ in range(t):
  n = int(input())
  out = min_coin(n)
  print(out)
