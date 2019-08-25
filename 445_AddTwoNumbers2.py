# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #Runtime: 52 ms, faster than 91.17% of Python online submissions for Add Two Numbers II.
        #Memory Usage: 12 MB, less than 6.67% of Python online submissions for Add Two Numbers II.
        # time:o(n) space:o(n)
        s1=[]
        s2=[]
        while l1 or l2:
            if l1:
                s1.append(l1.val)
                l1=l1.next
            if l2:
                s2.append(l2.val)
                l2=l2.next
        res= None
        carry=0
        while s1 and s2:
            tmp=s1.pop()+s2.pop()+carry
            carry=1 if tmp>9 else 0
            t=res
            res=ListNode(tmp%10)
            res.next=t
        head= s1 if s1 else s2
        while head:
            tmp=head.pop()+carry
            carry = 1 if tmp>9 else 0
            t= res
            res=ListNode(tmp%10)
            res.next=t
        if carry:
            t=res
            res=ListNode(1)
            res.next=t
        return res

