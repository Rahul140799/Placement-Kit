T = int(input())
for i in range(0,T):
    N = int(input())
    # print(N, flush=True)
    A = int(input())
    # print(A, flush=True)
    S = 2*(10**N)+A 
    print(S, flush=True)
    B = int(input())
    # print(B, flush=True)
    C = (10**N) - B
    print(C, flush=True)
    D = int(input())
    # print(D, flush=True)
    E = S-A-B-C-D
    print(E, flush=True)
    F = int(input())
    # print(F, flush=True)