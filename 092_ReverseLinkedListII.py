
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return head
        if m==n :
            return head

        number = 1
        pre = ListNode(-1)
        pre.next = head # save the pre node of the reversed sublist.
        Pre_total = pre # save the head of the list to return
        while head and number< m:
            if number == m-1:
                pre = head
                # save the point of the (m-1)th node
            head = head.next
            number += 1

        r_number = n-m
        # the sub list starts form the current head
        sub_head = head
        sub_tail = None
        pre_sub = head
        head = head.next
        while head and r_number>0:
            if r_number == 1:
                sub_tail = head# save the end node of the sublist
            # insert the node infront of the pre_ node
            next = head.next
            head.next = pre_sub
            pre_sub = head
            head = next
            r_number -= 1
        sub_head.next = head # the head of the sublist to be the end of the sublist
        pre.next = sub_tail # the end of the sublist to be the head of the sublist

        return Pre_total.next

if __name__ == '__main__':

    pre = ListNode(-1)
    pre.next = None

    for i in xrange(2):
        node = ListNode(i)
        node.next = 0
        if i == 0:
            pre.next = node
            head = node
            p = node
        else:
            p.next = node
            p = p.next


    print 'Input : ',
    t = head
    while t:
        print t.val,
        t = t.next
    print

    k = Solution()
    m = 1
    n = 2

    r = k.reverseBetween(head,m,n)
    print  'Result : ',
    while r:
        print r.val,
        r = r.next

    print



