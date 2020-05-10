class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        temp1 = head
        temp2 = head.next
        
        while temp2:
            if temp1.val == temp2.val:
                temp1.next = temp2.next
                temp2 = temp2.next
            else:
                temp1 = temp2
                temp2 = temp2.next
        return head

--------------------Explanation-------------------------

1 -> 1 -> 2 -> 3 -> 3
t1   t2

temp1 = head
temp2 = head.next

temp2 != None:
	t1 == t2
		t1 stayst at t1 ; whereas t1.next points to t2.next and t2 moves to t2.next.
	
	else:
		t1 is moved to t2 and t2 moves to t2.next 		
