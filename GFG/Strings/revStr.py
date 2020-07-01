def reverse(st):
    new_st = st.split('.')
    res = ""
    for i in range(len(new_st)-1,-1,-1):
        res += new_st[i]+'.'
    return res[:len(res)-1]

t = int(input())
for _ in range(t):
    st = input()
    out = reverse(st)
    print(out)
