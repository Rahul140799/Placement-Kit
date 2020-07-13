def covac(arr,cure,n):
  maxi = max(arr)
  days = 0
    
  if(cure >= maxi):
    return len(arr)
  
  else:
      arr.sort(reverse = True)
      
      while(n > 0):
        while(len(arr)!=0 and arr[-1] <= cure):
          x = arr.pop()
          days += 1
          n -= 1
          
          if x*2 >= cure:
            cure = x*2

        if len(arr)!=0:
          if(arr[0]-cure)*2 < arr[0]:
            arr[0] = (arr[0]-cure)*2
          days += 1
          cure *= 2

          if cure >= max(arr):
            days += len(arr)
            break

  return days

t = int(input())
for _ in range(t):
  n,x = map(int,input().split())
  arr = list(map(int,input().split()))
  out = covac(arr,x,n)
  print(out)
