# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
#Runtime: 80 ms, faster than 73.41% of Python online submissions for Linked List Random Node.
#Memory Usage: 16.1 MB, less than 66.18% of Python online submissions for Linked List Random Node.
import random
class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head,self.size= head,0
        while head!=None:
            self.size+=1
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        if self.head==None: return None
        i = random.randint(1,self.size)
        cur = self.head
        while i>1:
            cur= cur.next
            i-=1
        return cur.val




head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(400)
object = Solution(head)
print(object.getRandom())
