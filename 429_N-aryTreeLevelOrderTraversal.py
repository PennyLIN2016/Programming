
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        #Runtime: 688 ms, faster than 60.24% of Python online submissions for N-ary Tree Level Order Traversal.
        #Memory Usage: 107.5 MB, less than 85.71% of Python online submissions for N-ary Tree Level Order Traversal.
        # children is an array of nodes
        # time: o(n): n: the node number of the tree. space: 0(n)
        if not root: return []
        child=[]
        child.append(root)
        stack=[child]
        res=[]
        while stack:
            cur_level= stack.pop()
            cur_child=[]
            cur_root=[]
            for value in cur_level:
                cur_child.append(value.val)
                if value.children:
                    for i in value.children:
                        cur_root.append(i)
            if cur_root: stack.append(cur_root)
            res.append(cur_child)
        return res
    
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        #Runtime: 61 ms, faster than 37.88% of Python online submissions for N-ary Tree Level Order Traversal.
        # Memory Usage: 16.2 MB, less than 93.94% of Python online submissions for N-ary Tree Level Order Traversal.
        # time: o(n): the number of nodes space: o(n)
        if not root : return []
        stack= [root]
        res = [[root.val]]
        # trace the node by levels
        while stack:
            tmpNode = []
            childList = []
            for v in stack:
                for child in v.children:
                    tmpNode.append(child)
                    childList.append(child.val)
            stack = tmpNode
            if childList!= []:
                res.append(childList)
        return res






