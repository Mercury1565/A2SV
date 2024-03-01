# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)

        pointer_1 , pointer_2 = dummy , head
        '''
        Starting Position (@ == DUMMY NODE)
        @ -> 1 -> 2 -> 3 -> 4 -> 5 -> None
        ^    ^
        p1   p2
        '''

        for _ in range(left - 1):
            pointer_1 , pointer_2 = pointer_2 , pointer_2.next

        '''
        Left Node located with p2
        @ -> 1 -> 2 -> 3 -> 4 -> 5 -> None
             ^    ^
             p1   p2
        '''

        prev = None
        for _ in range(right - left + 1):
            temp = pointer_2.next
            pointer_2.next = prev

            prev = pointer_2
            pointer_2 = temp
        
        '''
        Reversal completed
                 None
                  ^
                  |
        @ -> 1 -> 2 <- 3 <- 4 -> 5 -> None
             ^             ^    ^
             p1           prev  p2
        '''

        pointer_1.next.next = pointer_2
        pointer_1.next = prev

        '''
        COMPLETE !
             -----------------
             |    -----------|--- 
             |    ^          |   |
             |    |          v   v
        @ -> 1    2 <- 3 <- 4 -> 5 -> None
             ^             ^    ^
             p1           prev  p2
        '''

        return dummy.next