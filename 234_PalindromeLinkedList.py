# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #Runtime: 64 ms, faster than 97.29% of Python online submissions for Palindrome Linked List.
        #Memory Usage: 30.9 MB, less than 46.20% of Python online submissions for Palindrome Linked List.
        if head is None: return True
        # get the middle pos
        fast=slow= head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        #reverse the second half
        p,last= slow.next,None
        while p:
            next = p.next
            p.next = last
            last,p = p,next
        #palindrome checking
        p1,p2=last,head
        while p1 and p1.val==p2.val:
            p1,p2= p1.next,p2.next
        return p1==None


if __name__ == '__main__':

    P1 = ListNode(0)
    P2 = ListNode(1)
    #P3 = ListNode(2)
    #P4 = ListNode(3)

    P1.next = P2
    #P2.next = P3
    #P3.next = P2

    k = Solution()

    if k.isPalindrome(P1):
        print ('Yes')
    else:
        print ('No')
