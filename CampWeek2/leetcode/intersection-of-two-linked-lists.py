 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        first = headA
        second = headB

        while first:
            seen.add(first)
            first = first.next

        while second:
            if second in seen:
                return second
            second = second.next
