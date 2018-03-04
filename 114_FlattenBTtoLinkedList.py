#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def next_faltten(root):
            if not root:
                return root

            r1 = next_faltten(root.left)
            r2 = next_faltten(root.right)

            if not r1 and not r2:
                return root
            if not r2:
                root.right = root.left
                root.left = None
                return r1

            if not r1:
                return r2

            tmp = root.right
            root.right = root.left
            root.left = None
            r1.right = tmp
            return r2

        next_faltten(root)





if __name__ == '__main__':
    root = TreeNode(10)
    """left = TreeNode(21)
    right = TreeNode(15)
    left_1 = TreeNode(6)
    left_2 = TreeNode(20)
    root.left= left
    root.right = right
    right.left = left_1
    right.right = left_2"""


    k = Solution()
    k.flatten(root)
    print root
