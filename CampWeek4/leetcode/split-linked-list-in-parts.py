# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        counter = ListNode(0 , head)
        count = 0

        while counter.next:
            count += 1
            counter = counter.next

        remainder = count % k
        length = count // k
        result = []
    
        while head:
            dummy = ListNode(0 , head)
            temp = dummy.next
            for _ in range(length):
                dummy = dummy.next
                head = head.next
            
            if remainder > 0:
                dummy = dummy.next
                head = head.next
                remainder -= 1

            dummy.next = None
            result.append(temp)

        while len(result) < k:
            result.append(ListNode(''))

        return result



        