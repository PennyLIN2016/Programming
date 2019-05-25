# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #Runtime: 8 ms, faster than 99.88% of Python online submissions for Invert Binary Tree.
#Memory Usage: 11.7 MB, less than 70.56% of Python online submissions for Invert Binary Tree
        if root==None: return root
        s = [root]
        while len(s)!=0:
            tmp=s.pop()
            tmp.left , tmp.right = tmp.right,tmp.left
            if tmp.left:s.append(tmp.left)
            if tmp.right:s.append(tmp.right)
        return root



if __name__ == '__main__':

    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t1.left=t2
    t2.left=t4
    t2.left=t5
    t1.right=t3
    t3.left=t6

    object = Solution()
    r = object.invertTree(t1)

    print(r)
    print('---End---')

