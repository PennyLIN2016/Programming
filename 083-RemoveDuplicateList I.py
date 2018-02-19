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

        tmp = head
        while tmp.next:
            if tmp.next.val != tmp.val:
                tmp = tmp.next
            else:
                tmp.next = tmp.next.next

        return head

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




