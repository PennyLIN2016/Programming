# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    '''
    # a solution with using extra space  79s
    def hasCycle(self, head): #
        """
        :type head: ListNode
        :rtype: bool
        """
        flag = set()

        pos = 0

        while head:
            if head in flag:
                return head
            flag.add(head)
            head = head.next
        return None
        '''

    def hasCycle(self, head):  # without using extra space(90s)
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = begin = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                while begin!= slow:
                    slow = slow.next
                    begin = begin.next
                return begin

        return None



if __name__ == '__main__':

    P1 = ListNode(0)
    P2 = ListNode(1)
    P3 = ListNode(2)
    P4 = ListNode(3)

    P1.next = P2
    P2.next = P3
    P3.next = P2

    k = Solution()

    print (k.hasCycle(P1).val) if k.hasCycle(P1) else print('None')