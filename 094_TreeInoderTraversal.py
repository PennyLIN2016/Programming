# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def sub_Traversal(s_t,r):
            if not s_t:
                return
            if s_t.left:
                sub_Traversal(s_t.left,r)
            r.append(s_t.val)
            sub_Traversal(s_t.right,r)

        r = []
        sub_Traversal(root,r)
        return r

if __name__ == '__main__':
    root = TreeNode(5)
    left = TreeNode(4)
    right = TreeNode(3)
    left_1 = TreeNode(2)
    left_2 = TreeNode(1)
    right_1 = TreeNode(0)
    root.left= left
    left.left = left_1
    left.right = left_2
    root.right = right
    right.left = right_1
    k = Solution()
    r = k.inorderTraversal(root)
    print r





