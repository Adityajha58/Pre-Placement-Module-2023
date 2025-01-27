class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            prev, current = head, head.next
            while prev is not None and current is not None:
                if prev.val == current.val:
                    prev.next = current.next
                else:
                    prev = prev.next
                current = current.next
        return head