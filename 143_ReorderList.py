# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    
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
