if head == None:
            return head
        
        count = 0
        
        fast = head
        while fast != None:
            fast = fast.next
            count += 1
        
        mid = count // 2 + 1
        
        slow = head
        for i in range(1, mid):
            slow = slow.next
            
        return slow