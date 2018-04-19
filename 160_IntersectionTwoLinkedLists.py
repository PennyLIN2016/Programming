# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    # my soltuion 368
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A = set()
        B = set()
        while headA or headB:
            if headA:
                if headA in B:
                    return headA
                A.add(headA)
                headA = headA.next

            if headB:
                if headB in A:
                    return headB
                B.add(headB)
                headB = headB.next

        return None




if __name__ == '__main__':
    P1 = ListNode(0)
    P2 = ListNode(1)
    P3 = ListNode(2)
    P4 = ListNode(3)
    P5 = ListNode(4)
    P6 = ListNode(5)
    P7 = ListNode(6)
    P8 = ListNode(7)

    P1.next = P2
    P2.next = P3
    P3.next = P4
    P4.next = P6
    P6.next = P7
    P7.next = P8

    P5.next = P3



    k = Solution()

    print(k.getIntersectionNode(P1,P5).val)





