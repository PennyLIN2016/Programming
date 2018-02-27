# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def compareTwoTree(root1,root2):
            if not root1 and not root2:
                return True
            if root1 and root2 and root1.val== root2.val:
                return compareTwoTree(root1.left,root2.right) and compareTwoTree(root1.right, root2.left)
            return False

        if root:
            return compareTwoTree(root.left,root.right)
        else:
            return True




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
    r = k.isSymmetric(root)
    print r





