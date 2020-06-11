def maxSubarraySumCircular(self, A: List[int]) -> int:
        k = self.kadane(A) 				#maximum subarray 
        
        s = 0
        for i in range(len(A)):
            s += A[i]					#calculate sum of all elements
            A[i] *= -1					#mulitply by -1 and sum all elements
        s = s + self.kadane(A)				#add it to the existing sum, in this way, we remove(-)ve values
        
        if s > k and s!=0:
            return s
        else:
            return k
        
    def kadane(self,A):
        current_sum = max_sum = A[0]
        for num in A[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(current_sum, max_sum)
        return max_sum

