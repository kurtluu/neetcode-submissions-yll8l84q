# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        
        l,r  = dummy, dummy
        
        # init r
        while n > 0:
            r = r.next
            n -= 1
        
        while r:
            r = r.next
            if r == None:
                l.next = l.next.next
            l = l.next

        return dummy.next