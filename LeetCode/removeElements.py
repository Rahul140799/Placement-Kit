class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        while head and head.val == val:
            head = head.next 
            
        if head == None:
            return None
        
        curr = head.next
        temp = head
        
        while(curr):
            if curr.val != val:
                temp = curr
                curr = curr.next
            else:
                temp.next = curr.next
                curr = curr.next
                
        return head
