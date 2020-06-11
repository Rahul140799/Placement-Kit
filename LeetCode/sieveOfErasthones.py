temp = [i for i in range(2,n)]
        #print(temp)
        for i in temp:
            if i > sqrt(n):
                break
            if i != 0:
                for j in range(i*i,n,i):
                    #print(j)
                    temp[j-2] = 0
                #print(temp)
        return len(temp) - temp.count(0)
