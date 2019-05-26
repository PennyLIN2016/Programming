# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # the bst definition : left<=root<=right
        #Runtime: 36 ms, faster than 99.01% of Python online submissions for Kth Smallest Element in a BST.
        #Memory Usage: 19.8 MB, less than 5.44% of Python online submissions for Kth Smallest Element in a BST.
        if not root: return -1
        s= []
        while root or len(s)!=0:
            while root:
                s.append(root)
                root= root.left
            root = s.pop()
            k-=1
            if k==0:
                return root.val
            else:
                root= root.right

        return -1

if __name__ == '__main__':

    t1 = TreeNode(1)
    t2 = TreeNode(7)
    t3 = TreeNode(0)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t1.left=t2
    t2.left=t4
    t2.left=t5
    t1.right=t3
    t3.left=t6
    k =3

    object = Solution()
    r = object.kthSmallest(t1,2)

    print(r)
    print('---End---')

