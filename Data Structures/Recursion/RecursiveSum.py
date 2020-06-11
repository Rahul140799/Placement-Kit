def rec_sum(n):
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)

n = int(input("Enter Number:"))
x = rec_sum(n)
print(x)