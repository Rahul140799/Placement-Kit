
subsets = []
n = 3

def search(k):
    if k == n:
        print(subsets)
    else:
        search(k+1)
        subsets.append(k)
        search(k+1)
        subsets.pop()

search(0)