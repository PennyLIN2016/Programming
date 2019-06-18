# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Runtime: 28 ms, faster than 92.07% of Python online submissions for Odd Even Linked List.
        #Memory Usage: 15.2 MB, less than 39.77% of Python online submissions for Odd Even Linked List
        # time:o(n/2) space:o(1)
        if not head or not head.next: return head
        odd_head,even_head,= head,head.next,
        pre_even= even_head
        pre_odd = odd_head
        head= head.next.next
        while head and head.next:
            pre_odd.next= head
            pre_even.next = head.next
            pre_odd = pre_odd.next
            pre_even = pre_even.next
            head= head.next.next

        if head:
            pre_odd.next = head
            pre_odd = pre_odd.next

        pre_odd.next= even_head
        pre_even.next= None
        return odd_head




if __name__ == '__main__':
    import sys
    k = Solution()
    l= ListNode(1)
    pre= l
    for i in range(2,5+1):
        p = ListNode(i)
        pre.next = p
        pre= pre.next
    t= l
    tmp=[]
    while l:
        tmp.append(l.val)
        l= l.next
    print('Before:  '+ str(tmp))

    r = k.oddEvenList(t)
    tmp=[]
    l= t
    while l:
        tmp.append(l.val)
        l= l.next
    print('After:    '+ str(tmp))
    print('---End---')



