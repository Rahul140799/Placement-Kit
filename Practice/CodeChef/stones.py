for i in range(int(input())):
    J = input()
    S = input()
    
    count = 0
    for i in range(len(S)):
        if S[i] in J:
            count+=1
    print(count)