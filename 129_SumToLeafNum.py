#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sum_subtrees(root,path,sum_num):
            path.append(root.val)
            if not root.left and not root.right:
                tmp = 0
                for i in xrange(len(path)):
                    tmp = tmp*10+ path[i]
                sum_num[0] += tmp
            if root.left:
                sum_subtrees(root.left,path,sum_num)
            if root.right:
                sum_subtrees(root.right,path,sum_num)
            path.pop()

        if not root:
            return 0
        sum_num = [0]
        sum_subtrees(root,[],sum_num)
        return  sum_num[0]


if __name__ == '__main__':

    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    left_1 = TreeNode(4)
    left_2 = TreeNode(5)
    root.left= left
    root.right = right
    right.left = left_1
    right.right = left_2


    k = Solution()
    r = k.sumNumbers(root)

    print r
