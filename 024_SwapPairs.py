# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        r = ListNode(-1)
        pre_head = r
        r.next = head
        while head:
            if not stack:
                stack.append(head)
                head =head.next
            else:
                r.next = head
                node = stack.pop()
                node.next = head.next
                r = node
                head.next = node
                if node:
                    head = node.next

        return pre_head.next


if __name__ == '__main__':

    list1 = []

    for i in xrange(2):
        node1 = ListNode(i+1)
        list1.append(node1)
        if i > 0:
            list1[i-1].next = node1
    print

    tmp1 = list1[0]
    print 'Input list :',
    while tmp1:
        print tmp1.val,
        tmp1=tmp1.next



    k = Solution()
    r = k.swapPairs(list1[0])

    tmp3 = r
    print'\n result :',
    while tmp3:
        print tmp3.val,
        tmp3 = tmp3.next
    print

    '''
    k = Solution()
    list_total= []
    list_total.append(ListNode(1))
    list_total.append(ListNode(0))
    r = k.mergeKLists(list_total)

    tmp3 = r
    print' result :',
    while tmp3:
        print tmp3.val,
        tmp3 = tmp3.next
    print
    '''



