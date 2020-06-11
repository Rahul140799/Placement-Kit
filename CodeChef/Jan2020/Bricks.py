
T = int(input())
for i in range(0,T):
    s,a,b,c = map(int, input().split())
    if s >= a+b+c:
        print(1)
    elif s>= a+b or s >= b+c:
        print(2)
    else:
        print(3)