# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        #Runtime: 996 ms, faster than 30.82% of Python online submissions for Path Sum III.
        #Memory Usage: 12.9 MB, less than 54.54% of Python online submissions for Path Sum III.
        # bfs+dfs solution:
        if not root: return 0
        res=[0]
        dq=collections.deque()
        dq.append(root)
        while dq:
            tmp=dq.popleft()
            if tmp.left:dq.append(tmp.left)
            if tmp.right:dq.append(tmp.right)
            self.NodeFind(tmp,sum,res)
        return res[0]
    def NodeFind(self,node,t,r):
        if not node:return
        t-=node.val
        if t==0 :
            r[0]+=1
        self.NodeFind(node.left,t,r)
        self.NodeFind(node.right,t,r)









if __name__ == '__main__':
    object = Solution()
    """
    n1=TreeNode(10)
    n2=TreeNode(5)
    n3=TreeNode(-3)
    n4=TreeNode(3)
    n5=TreeNode(2)
    n6=TreeNode(11)
    n7=TreeNode(3)
    n8=TreeNode(-2)
    n9=TreeNode(1)
    s= 8

    n1.left=n2
    n1.right=n3
    n3.right=n6
    n2.left=n4
    n2.right=n5
    n4.left=n7
    n4.right=n8
    n5.right=n9
    """
    n1=TreeNode(1)
    n2=TreeNode(-2)
    n3=TreeNode(-3)
    n4=TreeNode(1)
    n5=TreeNode(3)
    n6=TreeNode(-2)
    n7=None
    n8=TreeNode(-1)
    s= -1

    n1.left=n2
    n1.right=n3
    n2.left=n4
    n2.right=n5
    n3.left=n6
    n3.right=n7
    n4.left=n8

    r = object.pathSum(n1,s)
    print(r)
    print('---End---')
