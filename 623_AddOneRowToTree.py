# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
import collections
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        # Runtime: 40 ms, faster than 58.33% of Python online submissions for Add One Row to Tree.
        # Memory Usage: 14.7 MB, less than 100.00% of Python online submissions for Add One Row to Tree.
        # my own solution:
        if d==1:
            res=TreeNode(v)
            res.left=root
            return res
        if not root: return root
        res=root
        cur=1
        nodeq=[root]
        while cur<d-1 and nodeq:
            tmp=[]
            for node in nodeq:
                if node.left:tmp.append(node.left)
                if node.right:tmp.append(node.right)
            nodeq=tmp
            cur+=1

        for n in nodeq:
            print(n.val)
            left=TreeNode(v)
            right=TreeNode(v)
            left.left=n.left
            right.right=n.right
            n.left=left
            n.right=right
        return res

#####python3
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        ### Runtime: 59 ms, faster than 85.84% of Python3 online submissions for Add One Row to Tree.
        #Memory Usage: 16.6 MB, less than 92.18% of Python3 online submissions for Add One Row to Tree.
        # bfs solution: time: O(2**depth) space: o(2* depth)
        if depth == 1:
            newN = TreeNode(val)
            newN.left = root
            return newN
        stack = [root]
        while depth > 2:
            tmp = []
            for node in stack:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            depth -= 1
            stack = tmp
        for v in stack:
            # notes: no matter if the v.left/right is null, the new node should replace the right/left
            newN = TreeNode(val)
            newN.left = v.left
            v.left = newN
            newN = TreeNode(val)
            newN.right = v.right
            v.right = newN
        return root




if __name__ == '__main__':
    object = Solution()
    n1=None
    n2=2
    n3=3

    print('---Start---')
    print (n1)
    r = object.addOneRow(n1,n2,n3)
    print(r)
    print('---End---')
