def coin(I,N,Q):
    if N%2 == 0:
        print(N//2)
    else:
        if I == Q:
            print(N//2)
        else:
            print((N//2)+1)

t = int(input())
for _ in range(t):
    g = int(input())
    for _ in range(g):
        I,N,Q = map(int,input().split())
        out = coin(I,N,Q)
