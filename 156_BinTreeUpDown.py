# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
# a good solution
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        # the right node should be a leaf or empty. So there is not recursion for the right node.
        left = self.upsideDownBinaryTree(root.left)
        if root.left:
            root.left.right = root
            root.left.left = root.right
            root.left = root.right = None
        return left if left else root


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)


    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5


    k = Solution()

    t = k.upsideDownBinaryTree(n1)
    print (t.val)





