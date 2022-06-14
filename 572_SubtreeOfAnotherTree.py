# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def isSubtree1(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # Runtime: 292 ms, faster than 34.94% of Python online submissions for Subtree of Another Tree.
        # Memory Usage: 13.1 MB, less than 20.00% of Python online submissions for Subtree of Another Tree.
        # dfs+dfs solution: dfs/bfs time o(m*n) m: the number of edges in s, n:the number of edges in t,

        if not s and not t:return True
        if not s or not t: return False
        return self.isSame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def isSame(self,n1,n2):
        if not n1 and not n2: return True
        if not n1 or not n2 : return False
        return n1.val==n2.val and self.isSame(n1.left,n2.left) and self.isSame(n1.right,n2.right)

    def isSubtree(self, s, t):
        #Runtime: 276 ms, faster than 56.26% of Python online submissions for Subtree of Another Tree.
        #Memory Usage: 12.8 MB, less than 80.00% of Python online submissions for Subtree of Another Tree.
        # bfs+dfs solution
        import collections
        q=collections.deque()
        q.append(s)
        while q:
            cur=q.popleft()
            if not cur: continue
            if self.isSame(cur,t):return True
            q.append(cur.left)
            q.append(cur.right)
        return False
## python 3 solution
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # Runtime: 184 ms, faster than 40.70% of Python3 online submissions for Subtree of Another Tree.
        # Memory Usage: 15.1 MB, less than 34.71% of Python3 online submissions for Subtree of Another Tree.
        # dfs solution: time:o(n**2) space: o(1)
        def compareTwoTree(node1, node2):
            if not node1 and not node2:
                return True
            if (node1 and not node2) or (not node1 and node2):
                return False
            if node1.val != node2.val:
                return False
            return compareTwoTree(node1.left, node2.left) and compareTwoTree(node1.right, node2.right)
        if compareTwoTree(root, subRoot):
            return True
        if not root: return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1=TreeNode(3)
    n2=TreeNode(4)
    n3=TreeNode(5)
    n4=TreeNode(1)
    n5=TreeNode(2)
    n1.left=n2
    n1.right=n3
    n2.left=n4
    n2.right=n5

    t1 = TreeNode(4)
    t2 = TreeNode(1)
    t3 = TreeNode(2)
    t1.left = t2
    t1.right = t3



    print('---Start---')
    print (n1.val)
    r = object.isSubtree(n1,t1)
    print(r)
    print('---End---')
