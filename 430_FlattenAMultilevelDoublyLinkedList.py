# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # Runtime: 29 ms, faster than 82.64% of Python online submissions for Flatten a Multilevel Doubly Linked List.
        #Memory Usage: 14 MB, less than 71.24% of Python online submissions for Flatten a Multilevel Doubly Linked List.
        # use stack to implement dfs: time:o(n) space: o(n)
        if not head: return
        cur = head
        stack = []
        pre = None
        while cur or stack:

            if cur and cur.child:
                #print('cur1-{}'.format(cur.val))
                if cur.next:
                    stack.append(cur.next)
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None
                pre = cur
                cur = cur.next
            elif cur and not cur.child:
                #print('cur2-{}'.format(cur.val))
                pre = cur
                cur = cur.next
            elif not cur:
                nextNode = stack.pop()
                #print('nextNode: {}'.format(nextNode.val))
                #print('pre: {}'.format(pre.val))
                nextNode.prev = pre
                pre.next = nextNode
                cur = nextNode

        return head


if __name__ == '__main__':
    object = Solution()
    t1 = Node(2,None,None,None)
    print(t1)
    r = object.flatten(t1)
    print('---End---')
