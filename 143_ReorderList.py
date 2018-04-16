# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    '''
    # my solution: 11/13 Time Limit Exceed
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        def GetTail(root):

            while root.next:
                pre = root
                root = root.next
            pre.next = None
            return root

        p = head
        if not p:
            return head
        while p and p.next:
            tail = GetTail(p)
            tail.next = p.next
            p.next = tail
            p = tail.next
    '''
    # a good solution --100s
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        def reverse(root):
            pre = None
            cur = root
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        if not head or not head.next:
            return
        slow = fast = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if pre:
            pre.next = None
        # divide into two lists, one is the left half and the other is the right half. reverse the right half.
        newHead = reverse(slow)
        ret = dummy = ListNode(-1)
        p1 = head
        p2 = newHead
        # link the two lists together.
        while p1 and p2:
            dummy.next = p1
            p1 = p1.next
            dummy = dummy.next
            dummy.next = p2
            p2 = p2.next
            dummy = dummy.next

        if p2:
            dummy.next = p2
        head.next = ret.next.next


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
    k.reorderList(P1)


    print('After ------')

    t = P1
    while t:
        print(t.val)
        t = t.next