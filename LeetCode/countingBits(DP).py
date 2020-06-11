						Classic DP problem
result = [0]
        for i in range(1,num+1):
            result.append(result[i>>1] + int(i&1))
        return result

NOTE : 
	-> i>>1 (Right Shift Operation = i//2)
	-> int(i&1) => Logical AND of number with 1, if output = 0, it is even ; if output = 1, it is odd.
            

