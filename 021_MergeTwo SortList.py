# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp1 = l1
        tmp2 = l2

        if tmp1 and tmp2:
            r = ListNode(min(tmp1.val,tmp2.val))
        elif not tmp1:
            return tmp2
        else:
            return tmp1

        head = r
        while tmp1 and tmp2:
            if tmp1.val >= tmp2.val:
                r.next = tmp2
                r = r.next
                tmp2 = tmp2.next
            else:
                r.next = tmp1
                r = r.next
                tmp1 = tmp1.next

        if not tmp1:
            r.next = tmp2
        else:
            r.next = tmp1

        return  head.next


if __name__ == '__main__':
    list1 = []
    list2 = []

    for i in xrange(5):
        node1 = ListNode(i)
        list1.append(node1)
        node2= ListNode(i+1)
        list2.append(node2)
        if i > 0:
            list1[i-1].next = node1
            list2[i-1].next = node2
    print

    tmp1 = list1[0]
    print 'list 1:',
    while tmp1:
        print tmp1.val,
        tmp1=tmp1.next

    tmp2 = list2[0]
    print '\n list 2:',
    while tmp2:
        print tmp2.val,
        tmp2=tmp2.next


    k = Solution()
    r = k.mergeTwoLists(list1[0],list2[0])

    tmp3 = r
    print'\n result :',
    while tmp3:
        print tmp3.val,
        tmp3 = tmp3.next
    print





