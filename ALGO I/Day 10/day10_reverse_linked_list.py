# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Iteration approach
        # Run one pointer p in list. At each iteration:
        #     1. n = p.next
        #     2. p.next = n.next, jump cross n
        #     3. n.next = head, n prepend to the front
        #     4. head = n, reassign head

        if head == None:
            return None

        p = head
        while p.next:
            n = p.next
            p.next = n.next
            n.next = head
            head = n

        return head