# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    #Runtime: 68 ms, faster than 98.81% of Python online submissions for Count Complete Tree Nodes.
    #Memory Usage: 27.7 MB, less than 50.30% of Python online submissions for Count Complete Tree
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        def getheigh(root_node):
            h=0
            while root_node:
                root_node= root_node.left
                h+=1
            return h

        if not root: return 0
        count_num= 0
        left_h= getheigh(root.left)
        right_h= getheigh(root.right)
        if left_h==right_h:
            count_num = pow(2,left_h) + self.countNodes(root.right)
        else:
            count_num = pow(2,right_h) +self.countNodes(root.left)

        return count_num


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
    r = object.countNodes(t1)

    print(r)
    print('---End---')

