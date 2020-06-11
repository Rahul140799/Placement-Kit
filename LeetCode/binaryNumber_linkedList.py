#1
O(n)
st = ""
        while(head):
            st += str(head.val)
            head = head.next
        #print(st)
        return int(st,2)


#2
O(n^2)
cnt = -1
        tmp = head
        while(head):
            cnt+=1
            head = head.next
        #print(cnt)
        res = 0
        while(cnt>-1):
            res += (tmp.val)*pow(2,cnt)
            tmp = tmp.next
            #print("res:",res)
            cnt -= 1
        return res

#3
O(1) memory
res = head.val
        while(head.next):
            head = head.next
            res = (res<<1) | head.val
        return res



