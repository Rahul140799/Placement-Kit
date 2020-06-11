n = 3
chosen = [False] * (n+1)
permutation = []
permutations = []

def print_permutations():
    if len(permutation) == n:
        print(permutation)
        permutations.append(permutation)
    else:
        for i in range(1,n+1):
            if chosen[i] == True:
                continue
            chosen[i] = True
            permutation.append(i)
            print_permutations()
            chosen[i] = False
            permutation.pop()

