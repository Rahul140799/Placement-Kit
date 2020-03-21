def Solve (N):
    # Write your code here
    arr = []
    for i in range(1,N):
        if(N%i == 0):
            arr.append(i)
    s = sum(arr)
    if s == N:
        return "YES"
    else:
        return "NO"   

T = int(input())
for _ in range(T):
    N = int(input())
    out_ = Solve(N)
    print (out_)
