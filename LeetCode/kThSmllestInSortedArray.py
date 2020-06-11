import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                temp.append(matrix[i][j])
        heapq.heapify(temp)
        return heapq.nlargest(len(temp)-k+1,temp)[-1]
         
#Time complexity: O(N + (N-k+1)  Log(N-K+1) ) -> Max Heap is used	
		    |	    |	     |
		Number of |elem to   | Time taken to 	   
		elements  |          | Heapify
		in a list |search    |	

# For Min Heap : O(N + N(Log(N)) 

