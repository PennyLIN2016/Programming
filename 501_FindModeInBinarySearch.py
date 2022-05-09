import collections
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    #Runtime: 80 ms, faster than 8.36% of Python online submissions for Find Mode in Binary Search Tree.
    #Memory Usage: 19.8 MB, less than 44.44% of Python online submissions for Find Mode in Binary Search Tree.
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        self.count= collections.Counter()
        self.inOrder(root)
        freq= max(self.count.values())
        res=[]
        for value ,i in self.count.items():
            if i == freq:
                res.append(value)
        return res
    def inOrder(self,root):
        if not root:
            return
        self.inOrder(root.left)
        self.count[root.val]+=1
        self.inOrder(root.right)

    def findMode1(self, root:TreeNode)-> list[int]:
        # Runtime: 97 ms, faster than 25.96% of Python3 online submissions for Find Mode in Binary Search Tree.
        # Memory Usage: 18.5 MB, less than 41.95% of Python3 online submissions for Find Mode in Binary Search Tree.
        # brutal recursion solution space: o(n) time: (n)
        def dfs(curNode):
            if curNode.val not in freq:
                freq[curNode.val] = 1
            else:
                freq[curNode.val] += 1
            if curNode.left:
                dfs(curNode.left)
            if curNode.right:
                dfs(curNode.right)

        freq = {}
        dfs(root)
        res = []
        target = max(freq.values())
        for k in freq:
            if freq[k] == target:
                res.append(k)
        return res

    def findMode2(self, root:TreeNode)-> list[int]:
        # Runtime: 53 ms, faster than 93.92% of Python3 online submissions for Find Mode in Binary Search Tree.
        # Memory Usage: 17.9 MB, less than 92.33% of Python3 online submissions for Find Mode in Binary Search Tree.
        # no extra space(except for recursion stack) solution: space: O(1) time: o(n): node number
        # make use of the existing order series in bst
        res = []
        p, pre = root, None
        stack = []
        maxCnt, cnt = 0, 1
        while stack or p:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            if pre:
                cnt = cnt+1 if p.val == pre.val else 1
            if cnt >= maxCnt:
                if cnt > maxCnt:
                    res = [p.val]
                    maxCnt = cnt
                else:
                    res.append(p.val)
            pre = p
            p = p.right
        return res


