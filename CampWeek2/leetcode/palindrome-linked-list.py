# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        right = head
        left = None

        while right.next:
            right.prev = left

            left = right
            right = right.next

        right.prev = left
            
        while head:
            if head.val != right.val:
                return False
            
            head = head.next
            right = right.prev
        return True

        