
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def preorder1(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # Runtime: 48 ms, faster than 98.05% of Python online submissions for N-ary Tree Preorder Traversal.
        # Memory Usage: 14.8 MB, less than 100.00% of Python online submissions for N-ary Tree Preorder Traversal.
        # my own solution: time: o(n) space:o(n) recursion solution
        self.res=[]
        self.subPreorder(root)
        return self.res
    def subPreorder(self,node):
        if not node:return
        self.res.append(node.val)
        for value in node.children:
            self.subPreorder(value)

    def preorder(self, root):
        # my own iterative solution
        # Runtime: 44 ms, faster than 98.82% of Python online submissions for N-ary Tree Preorder Traversal.
        # Memory Usage: 14.9 MB, less than 100.00% of Python online submissions for N-ary Tree Preorder Traversal.
        # time: o(n) space o(n)
        if not root: return []
        res=[]
        stack=[]
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if not node.children: continue
            for i in range(len(node.children)-1,-1,-1):
                stack.append(node.children[i])
        return res
#######python 3 solution
    def preorder(self, root: Node) -> list[int]:
        # dfs solution:
        # Runtime: 115 ms, faster than 5.01% of Python3 online submissions for N-ary Tree Preorder Traversal.
        # Memory Usage: 16.1 MB, less than 65.43% of Python3 online submissions for N-ary Tree Preorder Traversal.
        # time: o(n: number of nodes) space: o(n)
        if not root:
            return []
        res = [root.val]
        for n in root.children:
            res += self.preorder(n)
        return res



if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1 =None
    print('---Start---')
    print (n1)
    r = object.preorder(n1)
    print(r)
    print('---End---')
