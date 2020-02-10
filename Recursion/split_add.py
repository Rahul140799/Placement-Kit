def split_add(n):
    if n == 0:
        return 0 
    else:
        r = n%10
        q = n/10
        return r + split_add(q)
n = int(input("Enter a number:"))
x = split_add(n)
print(x)
