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
        #Runtime: 64 ms, faster than 98.35% of Python online submissions for Lowest Common Ancestor of a Binary Search Tree.
        #Memory Usage: 19.9 MB, less than 77.62% of Python online submissions for Lowest Common Ancestor of a Binary Search Tree.
        min_n= min(p.val,q.val)
        max_n= max(p.val,q.val)
        while root:
            if root.val<=max_n and root.val>=min_n:
                return root
            elif root.val<min_n:
                root=root.right
            else:
                root= root.left
        return None

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

