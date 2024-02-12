# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        dummy = newList
        
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            
            newList.next = head
            head = head.next
            newList = newList.next

        return dummy.next

        