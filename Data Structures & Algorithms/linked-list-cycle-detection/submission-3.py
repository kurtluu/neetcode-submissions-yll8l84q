# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hasSet = set()

        curr = head

        while curr:
            if curr not in hasSet:
                hasSet.add(curr)
            else:
                return True
            curr = curr.next
        return False
            
