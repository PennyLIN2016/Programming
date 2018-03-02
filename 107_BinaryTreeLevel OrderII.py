# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # iterative solution
        if not root:
            return []
        s = [[root.val]]
        queue = deque([root])
        while queue:
            level_s = []
            for i in xrange(len(queue)):
                # the the queue order,
                node = queue.popleft()
                if node.left:
                    level_s.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    level_s.append(node.right.val)
                    queue.append(node.right)
            if level_s:
                s.append(level_s)

        return  s[::-1]


if __name__ == '__main__':
    root = TreeNode(10)
    left = TreeNode(5)
    right = TreeNode(15)
    left_1 = TreeNode(6)
    left_2 = TreeNode(20)
    root.left= left
    root.right = right
    right.left = left_1
    right.right = left_2

    #root1 = TreeNode(1)
    #left1 = TreeNode(1)
    # root1.left= left1

    k = Solution()
    r = k.levelOrderBottom(root)
    print r





