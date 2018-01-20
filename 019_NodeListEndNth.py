
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if n == 0:
            print 'incorrect input parameters'
            return None

        tmp_right = head
        tmp_left= head
        l= n
        while l > 0 and tmp_right :
            # keep the gap of n
            tmp_right = tmp_right.next
            l -=1

        if not tmp_right:
            if l == 0:
                # the list has n items
                return head.next
            else:
                # the length of the list is less than n
                print 'incorrect input parameters'
                return None

        while tmp_right.next:
            # the length of the list is more than n
            tmp_right = tmp_right.next
            tmp_left = tmp_left.next

        tmp_left.next = tmp_left.next.next
        return head




if __name__ == '__main__':

    inputs =[]
    for i in xrange(2):
        node = ListNode(i)
        inputs.append(node)
        if i>0:
            inputs[i-1].next = node


    t = inputs[0]
    print 'Input : ',
    while t:
        print t.val,
        t = t.next
    print

    k = Solution()

    r = k.removeNthFromEnd(inputs[0],2)
    print  'Result : ',
    while r:
        print r.val,
        r = r.next

    print



