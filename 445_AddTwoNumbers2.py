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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Runtime: 69 ms, faster than 68.09% of Python online submissions for Add Two Numbers II.
        # Memory Usage: 13.5 MB, less than 66.90% of Python online submissions for Add Two Numbers II.
        # Solution: o(n) space:o(n)
        if not l1 : return l2
        stack1 = []
        stack2 = []
        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1 = l1.next
            if l2:
                stack2.append(l2.val)
                l2 = l2.next
        carry = 0
        pre = None
        while stack1 or stack2 or carry == 1:
            sumVal = carry
            if stack1:
                sumVal += stack1.pop()
            if stack2:
                sumVal += stack2.pop()
            cur = ListNode()
            if sumVal > 9:
                carry = 1
                cur.val = sumVal - 10
            else:
                carry = 0
                cur.val = sumVal
            cur.next = pre
            pre = cur
        return pre
