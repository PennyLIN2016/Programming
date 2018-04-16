# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # a good solution 192s
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = ListNode(-1)
        pre.next = head
        p = head
        while p and p.next:
            if p.next.val>= p.val:
                p = p.next
            else:
                tmp = p.next
                p .next = p.next.next
                p2 = pre
                while p2.next.val< tmp.val:
                    p2 = p2.next
                tmp.next = p2.next
                p2.next = tmp
        return pre.next



if __name__ == '__main__':

    P1 = ListNode(9)
    P2 = ListNode(1)
    P3 = ListNode(2)
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
    r = k.insertionSortList(P1)

    t = r
    while t:
        print(t.val)
        t = t.next
