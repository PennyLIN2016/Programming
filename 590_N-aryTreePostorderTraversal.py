
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def postorder1(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # my own recursive  solution time:o(n) space:o(n)
        # Runtime: 48 ms, faster than 97.86% of Python online submissions for N-ary Tree Postorder Traversal.
        # Memory Usage: 14.8 MB, less than 100.00% of Python online submissions for N-ary Tree Postorder Traversal.
        self.res=[]
        self.subPostorder(root)
        return self.res
    def subPostorder(self,node):
        if not node:return
        for value in node.children:
            self.subPostorder(value)
        self.res.append(node.val)

    def postorder(self, root):
        # my own iterative solution time: o(nlgn) space: o(n)
        # Runtime: 44 ms, faster than 98.43% of Python online submissions for N-ary Tree Postorder Traversal.
        # Memory Usage: 14.8 MB, less than 100.00% of Python online submissions for N-ary Tree Postorder Traversal.
        if not root :return
        stack,res=[],[]
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            for value in node.children:
                stack.append(value)
        return res[::-1]




if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1 =None
    print('---Start---')
    print (n1)
    r = object.postorder(n1)
    print(r)
    print('---End---')