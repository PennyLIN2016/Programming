# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        p = head
        while p:
            tmp = RandomListNode(p.label)
            tmp.next = p.next
            p.next = tmp
            p = tmp.next

        p = head
        while p:
            p.next.random = p.random and p.random.next
            p = p.next.next

        p = head
        copy = r_p = head and head.next
        while p:
            p.next = p = copy.next
            copy.next = copy = p and p.next
        return r_p


