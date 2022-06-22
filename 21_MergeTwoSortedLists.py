# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Runtime: 47 ms, faster than 70.01% of Python3 online submissions for Merge Two Sorted Lists.
        # Memory Usage: 13.9 MB, less than 31.83% of Python3 online submissions for Merge Two Sorted Lists.
        # time: O(len(list1) + len(list2)) space: o(1)
        if not list1:
            return list2
        if not list2:
            return list1
        pre = ListNode(val=0)
        head = pre
        while list1 and list2:
            #print('list1: {} list2: {}'.format(list1.val, list2.val))
            if list1.val <= list2.val:
                pre.next = list1
                pre = pre.next
                list1 = list1.next
            else:
                pre.next = list2
                pre = pre.next
                list2 = list2.next
        if list1:
            pre.next = list1
        else:
            pre.next = list2
        return head.next

