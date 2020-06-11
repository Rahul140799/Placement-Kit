def eoeo(ts):
    if ts%2 != 0:
        return ts//2
    else:
        while(ts>>1):
            if (ts>>1)%2 != 0:
                if ts == 2:
                  return 0
                return (ts>>1)//2
            else:
                ts = ts>>1

t = int(input())
for _ in range(t):
    ts = int(input())
    out = eoeo(ts)
    print(out)
