def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        odd = head
        even = head.next
        evenHead = even
        
        while(even and even.next):
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next
        
        odd.next  = evenHead
        
        return head
        
