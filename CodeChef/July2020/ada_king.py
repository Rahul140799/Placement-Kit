def king(k,arr):
    flag = 0
    for i in range(8):
        for j in range(8):
            if k > 0:
                arr[i][j] = '.'
                k -= 1
            
            if k == 0:
                flag = 1
                break
            
        if flag == 1:
            break
    
    arr[0][0] = 'O'
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j],end="")
        print()
    
t = int(input())
for _ in range(t):
    k = int(input())
    arr = [['X' for i in range(8)] for j in range(8)] 
    king(k,arr)
