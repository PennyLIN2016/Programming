import collections
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    #Runtime: 80 ms, faster than 8.36% of Python online submissions for Find Mode in Binary Search Tree.
    #Memory Usage: 19.8 MB, less than 44.44% of Python online submissions for Find Mode in Binary Search Tree.
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        self.count= collections.Counter()
        self.inOrder(root)
        freq= max(self.count.values())
        res=[]
        for value ,i in self.count.items():
            if i == freq:
                res.append(value)
        return res
    def inOrder(self,root):
        if not root:
            return
        self.inOrder(root.left)
        self.count[root.val]+=1
        self.inOrder(root.right)




