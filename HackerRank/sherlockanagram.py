def sherlockAndAnagrams(s):
    
    res = []
    for i in range(len(s)):
        temp = ""
        for j in range(i,len(s)):
            temp += s[j]
            res.append(temp)
    #print("1",res)
    cnt = 0
    for i in range(len(res)):
        res[i] = "".join(sorted(res[i]))
    #print("2",res)
    temp = sorted(res)
    #print("3",temp)
    for i in range(len(temp)-1):
        for j in range(i+1,len(temp)):
            if temp[i] == temp[j]:
                cnt += 1
            else:
                break
    return cnt
