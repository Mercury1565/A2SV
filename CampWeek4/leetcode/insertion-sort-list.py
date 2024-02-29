# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev , curr = head , head.next

        while curr:
            if curr.val >= prev.val:
                prev , curr = curr , curr.next
                continue

            compared_to = dummy

            # We look for a position to insert the relocated node by traversing from the very begining
            while curr.val > compared_to.next.val:
                compared_to = compared_to.next
            
            prev.next = curr.next  # Node removed from original position

            # Node inserted into its brand new position
            curr.next = compared_to.next
            compared_to.next = curr

            curr = prev.next
                
        return dummy.next
                    
                    
                    

                


        