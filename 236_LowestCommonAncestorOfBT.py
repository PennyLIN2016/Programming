# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #Runtime: 60 ms, faster than 97.91% of Python online submissions for Lowest Common Ancestor of a Binary Tree.
        #Memory Usage: 24 MB, less than 74.09% of Python online submissions for Lowest Common Ancestor of a Binary Tree.
        if not root or root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right= self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left if left else right


if __name__ == '__main__':
    #[6,2,8,0,4,7,9,null,null,3,5]

    t1 = TreeNode(6)
    t2 = TreeNode(2)
    t3 = TreeNode(8)
    t4 = TreeNode(0)
    t5 = TreeNode(4)
    t6 = TreeNode(7)
    t1.left=t2
    t2.left=t4
    t2.left=t5
    t1.right=t3

    t3.left=t6


    object = Solution()
    r = object.lowestCommonAncestor(t1,t4,t3)

    print(r.val)
    print('---End---')

