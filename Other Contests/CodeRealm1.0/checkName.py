def check(types):
    for i in types:
        if i not in vowels and types.count(i)>name.count(i):
            return False
        else:
            flag = 1
    
    if flag == 1:
        return True

name, typed = input().split()
vowels = ['a','e','i','o','u']

types = list(typed) 

out = check(types)
print(out)

