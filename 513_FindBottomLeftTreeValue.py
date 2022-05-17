# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
import collections
class Solution(object):
    def findBottomLeftValue1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #time : 32 ms, faster than 78.51% of Python online submissions for Find Bottom Left Tree Value.
        #Memory Usage: 16.3 MB, less than 40.00% of Python online submissions for Find Bottom Left Tree Value.
        s=[root]
        res=root
        while s:
            tmp=[]
            for value in s:
                if value.left: tmp.append(value.left)
                if value.right:tmp.append(value.right)
            if tmp:
                res=tmp[0]
            s=tmp
        return res.val
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # deque solution: deque: two-ended list or queue
        q=collections.deque()
        q.append(root)
        child=[[root.val]]
        while q:
            l=len(q)
            level=[]
            for i in range(l):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    level.append(node.right.val)
                if level:
                    child.append(level)
        return child[-1][0]

    def findBottomLeftValue(self, root: TreeNode) -> int:
        #Runtime: 59 ms, faster than 52.25% of Python3 online submissions for Find Bottom Left Tree Value.
        # Memory Usage: 16.3 MB, less than 60.41% of Python3 online submissions for Find Bottom Left Tree Value.
        # dfs+ wfs: time: o(n) space: (n)
        stack = [root]
        while stack:
            rowStack = []
            for v in stack:
                print('1-{}'.format(v.val))
                if v.left:
                    rowStack.append(v.left)
                    print('left-{}'.format(v.left.val))
                if v.right:
                    rowStack.append(v.right)
                    print('right-{}'.format(v.right.val))
            if rowStack == []:
                return stack[0].val
            stack = rowStack


if __name__ == '__main__':
    object = Solution()
    A= TreeNode(2)
    n1=TreeNode(1)
    n2=TreeNode(3)
    A.left=n1
    A.right=n2
    print('---Start---')
    print A.val
    r = object.findBottomLeftValue(A)
    print(r)
    print('---End---')
