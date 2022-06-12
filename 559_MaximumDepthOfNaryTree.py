# Definition for a binary tree node.
class Node(object):
     def __init__(self, val, children):
         self.val = val
     # children : node list
         self.children= children
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        #Runtime: 660 ms, faster than 94.44% of Python online submissions for Maximum Depth of N-ary Tree.
        #Memory Usage: 107.7 MB, less than 56.67% of Python online submissions for Maximum Depth of N-ary Tree.
        # my own solution: bfs: time : o(n) n: the number of nodes space: o(n)
        if not root:return 0
        levelNode=[root]
        res=0
        while levelNode:
            res+=1
            curLevel=[]
            for value in levelNode:
                if value.children:
                    for node in value.children:
                        curLevel.append(node)
            levelNode=curLevel
        return res

if __name__ == '__main__':
    object = Solution()
    n1=None


    print('---Start---')

    r = object.maxDepth(n1)
    print(r)
    print('---End---')
