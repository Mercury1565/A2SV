# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        new_list = ListNode()   

        dummy.next = new_list

        while list1 and list2:
            if list1.val <= list2.val:
                new_list.next = list1
                new_list = new_list.next
                list1 = list1.next
            else:
                new_list.next = list2
                new_list = new_list.next
                list2 = list2.next
        
        while list1:
            new_list.next = list1
            new_list = new_list.next
            list1 = list1.next
        while list2:
            new_list.next = list2
            new_list = new_list.next
            list2 = list2.next

        return dummy.next.next

        