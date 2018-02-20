# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head

        pre = ListNode(-1)
        pre.next = head

        before = ListNode(-1)
        tmp_before = before
        tmp = pre
        while tmp and tmp.next:
            if tmp.next.val < x :
                tmp_before.next = tmp.next
                tmp.next = tmp.next.next
                tmp_before = tmp_before.next
            else:
                # keep the numbers no less than x in the original list
                tmp = tmp.next
        # merge the two list into one
        tmp_before.next = pre.next

        return before.next

if __name__ == '__main__':

    head = None
    for i in range(3):
        t = ListNode((2*i))
        t.next = head
        head = t

    for i in reversed(range(2)):
        t = ListNode((3*i))
        t.next = head
        head = t
        tmp = head
    while tmp:
        print tmp.val,'->',
        tmp = tmp.next


    A = Solution()
    x = 3
    r = A.partition(head,3)

    print 'Result:',
    while r:
        print r.val,'->',
        r = r.next





