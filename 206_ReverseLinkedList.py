# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #  Runtime: 24 ms, faster than 91.82% of Python online submissions for Reverse Linked List.
        # Memory Usage: 13.6 MB, less than 25.52% of Python online submissions for Reverse Linked List.


        if head==None:
            return head
        r_head = None

        while head != None:
            next_head = head.next
            head.next = r_head
            r_head = head
            head = next_head
        return(r_head)

if __name__ == '__main__':

    P1 = ListNode(1)
    P2 = ListNode(2)
    P3 = ListNode(3)
    P4 = ListNode(4)

    P1.next = P2
    P2.next = P3
    P3.next = P4

    t = P1
    while t:
        print(t.val)
        t = t.next

    print('before---')

    k = Solution()
    r = k.reverseList(P1)

    t = r
    while t:
        print(t.val)
        t = t.next
    print('after---')
