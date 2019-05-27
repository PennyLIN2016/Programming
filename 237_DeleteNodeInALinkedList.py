# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Runtime: 16 ms, faster than 99.86% of Python online submissions for Delete Node in a Linked List.
        # Memory Usage: 12.4 MB, less than 31.61% of Python online submissions for Delete Node in a Linked List.
        node.val = node.next.val
        node.next= node.next.next

if __name__ == '__main__':
    nums = [4,5,1,9]
    head= None

    for i in range(len(nums)):
        if i ==0:
            head= ListNode(nums[i])
            head.next = None
            pre= head
        else:
            tmp= ListNode(nums[i])
            pre.next = tmp
            pre= tmp


    p = Solution()
    p.deleteNode(head)
    print(head.val)