# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = None
        first = head

        if not first:
            return head

        second = head.next

        while second:
            first.next = left
            temp = second.next
            second.next = first

            left = first
            first = second
            second = temp

        return first
            
    

      
            
        