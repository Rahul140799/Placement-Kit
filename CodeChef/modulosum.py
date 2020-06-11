a = int(input())

for i in range(0,a):
   
	 n, m = map(int, input().split())
   
	 
count = 0
    
    
	 for i in range(1,n+1):

	        count = count + (i**i)
 
       
  answer = count%m
   
	 print(answer)