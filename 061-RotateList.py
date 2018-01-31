# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None

        start = head
        stack_t = []
        while start.next:
            stack_t.append(start)
            start= start.next
        stack_t.append(start)
        k = k % len(stack_t)
        if k == 0:
            return head
        stack_t[-1].next = head
        head = stack_t[-k]
        stack_t[-(k+1)].next = None

        return head


if __name__ == '__main__':

    #inputs = raw_input('input the N :  ')

    head = None
    for i in reversed(range(int(1))):
        t = ListNode(i+1)
        t.next = head
        head = t

    A = Solution()
    k = 2
    r = A.rotateRight(head,k)

    print 'Result:',
    while r:
        print r.val,'->',
        r = r.next
    print 'NULL'




