# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Runtime: 20 ms, faster than 73.79% of Python online submissions for Sum of Left Leaves.
        #Memory Usage: 12.1 MB, less than 91.67% of Python online submissions for Sum of Left Leaves.
        # time: 0(n)  space:o(n)
        if not root: return 0
        res=0
        stack=[(root,0)]
        while stack:
            tmp,flag=stack.pop()
            # only accumulate the left leaves
            if flag and not tmp.left and not tmp.right:
                res+=tmp.val
            if tmp.left:stack.append((tmp.left,1))
            if tmp.right:stack.append((tmp.right,0))
        return res
    
   def sumOfLeftLeaves1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Runtime: 25 ms, faster than 62.32% of Python online submissions for Sum of Left Leaves.
        #Memory Usage: 14 MB, less than 68.84% of Python online submissions for Sum of Left Leaves.
        import collections
        if not root: return 0
        res = 0
        dq = collections.deque([(root, False)])
        while dq:
            node, left = dq.popleft()
            if not node.left and not node.right and left:
                res += node.val
            if node.left:
                dq.append([node.left, True])
            if node.right:
                dq.append([node.right, False])
        return res

if __name__ == '__main__':
    object = Solution()
    n1=TreeNode(3)
    n2=TreeNode(9)
    n3=TreeNode(20)
    n4=TreeNode(15)
    n5=TreeNode(7)
    """
    n1.left=n2
    n1.right=n3
    n3.left=n4
    n3.right=n5
    """

    r = object.sumOfLeftLeaves(n1)
    print(r)
    print('---End---')
