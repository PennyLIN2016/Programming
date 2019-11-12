# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Runtime: 736 ms, faster than 8.40% of Python online submissions for Diameter of Binary Tree.
        #Memory Usage: 15.1 MB, less than 7.69% of Python online submissions for Diameter of Binary Tree.
        def getDepth(node):
            if not node: return 0
            res= max(getDepth(node.left),getDepth(node.right))
            return 1+res
        if not root: return 0
        r=getDepth(root.left)+getDepth(root.right)
        # for non-even tree
        return max(r,max(self.diameterOfBinaryTree(root.right),self.diameterOfBinaryTree(root.left)))


if __name__ == '__main__':
    object = Solution()
    n1=TreeNode(1)
    n2=TreeNode(2)
    n1.left=n2
    n3=TreeNode(3)
    n2.right=n3
    n4=TreeNode(4)
    n2.left=n4
    n5=TreeNode(5)
    n2.right=n5


    print('---Start---')
    print n1.val
    r = object.diameterOfBinaryTree(n1)
    print(r)
    print('---End---')
