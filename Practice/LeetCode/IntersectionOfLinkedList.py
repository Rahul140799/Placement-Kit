# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        countA = 0
        countB = 0
        
        pA = headA
        pB = headB
        
        
        while(pA):
            countA += 1
            pA = pA.next
        while(pB):
            countB += 1
            pB = pB.next
            
        pA = headA
        pB = headB
        
        while countA > countB:
            pA = pA.next
            countA -= 1
            
        while countB > countA:
            pB = pB.next
            countB -= 1
            
        
        while(pA != pB):
            pA=pA.next 
            pB=pB.next
        return pA
        
