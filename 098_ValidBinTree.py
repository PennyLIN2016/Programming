# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_tree(root):
            r = [0]*3

            r[0] = root.val# min of this subtree
            r[1] = root.val# max of this subtree
            r[2] = 1 # the default is True

            if root.left:
                r_left = check_tree(root.left)
                if r_left[2] == 0:
                    r[2] = 0
                    return r
                if r_left[1]>= root.val:
                    r[2]= 0
                    return r

                r[0] = min(r_left[0],root.left.val)
                r[1] = max(r_left[1],root.left.val,r[1])
            if root.right:
                r_right = check_tree(root.right)
                if r_right[2] == 0:
                    r[2] = 0
                    return r
                if r_right[1]<= root.val:
                    r[2]= 0
                    return r

                r[0] = min(r[0],root.right.val,r_right[0])
                r[1] = max(root.right.val,r_right[1])

            return r


        if not root:
            return True
        if root.left:
            r = check_tree(root.left)
            if r[2]== 0:
                return False
            if r[1] >= root.val :
                return False
        if root.right:
            r = check_tree(root.right)
            if r[2]== 0:
                return False
            if r[0] <=  root.val :
                 return False
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

    '''root = TreeNode(1)
    left = TreeNode(1)

    root.left= left'''


    k = Solution()
    r = k.isValidBST(root)
    print r





