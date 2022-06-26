# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    # Runtime: 54 ms, faster than 78.17% of Python online submissions for Binary Tree Tilt.
    # Memory Usage: 16.2 MB, less than 38.03% of Python online submissions for Binary Tree Tilt.
    # time: o(n) all nodes space: o(1): ignore the stack of dfs
    def __init__(self):
        self._tilt = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self._tilt += abs(left - right)
            return node.val + left + right

        dfs(root)
        return self._tilt






obj = Solution()
t1 = None
#t1 = "1-11"
print(t1)
print(obj.Solution(t1))


