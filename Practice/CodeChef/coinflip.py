for i in range(0,int(input())):
    for g in range(0,int(input())):
        I,N,Q = map(int,input().split())
        x = N//2
        if I == 1:
            if Q == 1:
                print(N//2)
            else:
                print(N-(N//2))
        if I == 2:
            if Q == 1:
                print(N-(N//2))
            else:
                print(N//2)