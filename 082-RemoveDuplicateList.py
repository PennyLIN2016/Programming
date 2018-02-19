# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return  head

        pre_head = ListNode(-1)
        pre_head.next = head


        tmp = pre_head
        while tmp.next:
            if tmp.next.next and tmp.next.val == tmp.next.next.val:
                tmp_next = tmp.next
                while tmp_next and tmp_next.next and tmp_next.val ==tmp_next.next.val:
                    tmp_next = tmp_next.next
                tmp.next =tmp_next.next
            else:
                tmp = tmp.next

        return pre_head.next

if __name__ == '__main__':

    head = None
    for i in reversed(range(int(1))):
        t = ListNode((i))
        t.next = head
        head = t

    A = Solution()
    r = A.deleteDuplicates(head)

    print 'Result:',
    while r:
        print r.val,'->',
        r = r.next
    print 'NULL'




