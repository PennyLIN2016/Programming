# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def nextMaxDepth(Node):
            r1,r2 = 0, 0
            if  Node.left:
                r1 = nextMaxDepth(Node.left)
            if Node.right:
                r2 = nextMaxDepth(Node.right)
            return 1+ max(r1,r2)

        if not root:
            return 0
        # or  return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return nextMaxDepth(root)


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
    r = k.maxDepth(root)
    print r





