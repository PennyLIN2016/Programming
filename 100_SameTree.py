# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def checkTwoTree(t1,t2):
            if t1.val!= t2.val:
                return False
            if (t1.left == None and t2.left!= None) or (t1.left != None and t2.left == None):
                return False
            if t1.left and t2.left:
                if not checkTwoTree(t1.left,t2.left):
                    return False

            if (t1.right == None and t2.right!= None) or (t1.right != None and t2.right == None):
                return False
            if t1.right and t2.right:
                if not checkTwoTree(t1.right,t2.right):
                    return False

            return True

        if p and q:
            return checkTwoTree(p,q)
        elif not p and not q:
            return True
        else:
            return False



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

    root1 = TreeNode(1)
    left1 = TreeNode(1)

    root1.left= left1


    k = Solution()
    r = k.isSameTree(root,root1)
    print r





