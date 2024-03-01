# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less , great = ListNode(0) , ListNode(0)
        less_pointer , great_pointer = less , great

        while head:
            if head.val < x:
                less_pointer.next = head
                less_pointer = less_pointer.next
            else:
                great_pointer.next = head
                great_pointer = great_pointer.next
            head = head.next

        great_pointer.next = None
        less_pointer.next = great.next

        return less.next

       
        