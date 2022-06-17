# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # Runtime: 68 ms, faster than 59.72% of Python online submissions for Merge Two Binary Trees.
        # Memory Usage: 12.9 MB, less than 33.33% of Python online submissions for Merge Two Binary Trees.
        # my own solution: dfs recursion
        if not t1: return t2
        if not t2: return t1
        t1.val+=t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right=self.mergeTrees(t1.right,t2.right)

        return t1

#########python3
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # Runtime: 93 ms, faster than 83.61% of Python3 online submissions for Merge Two Binary Trees.
        # Memory Usage: 15.6 MB, less than 18.27% of Python3 online submissions for Merge Two Binary Trees.
        # time:o(max(n1, n2)) space: o(max(n1, n2)) : recursion stack
        if not root1: return root2
        if not root2: return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1

if __name__ == '__main__':
    object = Solution()
    n1=None
    n2=None

    print('---Start---')
    print (n1)
    r = object.mergeTrees(n1,n2)
    print(r)
    print('---End---')
