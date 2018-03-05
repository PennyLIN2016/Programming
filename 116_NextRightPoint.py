# Definition for binary tree with next pointer.
class TreeLinkNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         self.next = None
from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        if not root:
            return root
        root.next = None
        queue = deque([root])

        while queue:
            l = len(queue)
            for i in xrange(l):
                tmp = queue.popleft()
                if l == 1:
                    tmp.next = None
                elif i == 0:
                    pre = tmp
                elif i < l-1:
                    pre.next = tmp
                    pre = tmp
                else:
                    pre.next = tmp
                    tmp.next = None

                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)



if __name__ == '__main__':
    root = TreeLinkNode(10)
    left = TreeLinkNode(21)
    right = TreeLinkNode(15)
    left_1 = TreeLinkNode(6)
    left_2 = TreeLinkNode(20)
    root.left= left
    root.right = right
    right.left = left_1
    right.right = left_2


    k = Solution()
    k.connect(root)

    print root

