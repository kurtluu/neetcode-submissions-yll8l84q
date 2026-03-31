# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head.next

        # find middle
        while f and f.next:
            s = s.next
            f = f.next.next
        
        # reverse last half        
        second = s.next
        s.next = None 
        prev = None 

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        # merge both halves
        first = head
        second = prev

        while second:
            nxt1 = first.next
            nxt2 = second.next

            first.next = second
            second.next = nxt1

            first = nxt1
            second = nxt2


        

        


        