# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Runtime: 44 ms, faster than 85.13% of Python online submissions for Minimum Absolute Difference in BST.
        # Memory Usage: 15.9 MB, less than 50.00% of Python online submissions for Minimum Absolute Difference in BST.
        # my own solution: time: o(n) space:o(n)
        def getList(node):
            if not node:
                return []
            res=getList(node.left)+[node.val]+getList(node.right)
            return res

        r= getList(root)
        minD=float('inf')
        for i,value in enumerate(r):
            if i==0: continue
            minD = min(minD,value-r[i-1])
        return minD

    def getMinimumDifference(self, root: [TreeNode]) -> int:
        # Runtime: 67 ms, faster than 65.72% of Python3 online submissions for Minimum Absolute Difference in BST.
        # Memory Usage: 16.3 MB, less than 22.77% of Python3 online submissions for Minimum Absolute Difference in BST.
        # time: o(n) space: o(n)
        def findPath(node):
            if not node:
                return
            path = [node.val]
            if node.left:
                path = findPath(node.left) + path
            if node.right:
                path = path + findPath(node.right)
            return path

        treeList = findPath(root)
        print(treeList)

        res = abs(treeList[1] - treeList[0])
        for i in range(len(treeList)):
            res = min(res, abs(treeList[i] - treeList[i - 1]))

        return res


if __name__ == '__main__':
    object = Solution()
    n1=TreeNode(1)
    n2=TreeNode(3)
    n1.right=n2
    n3=TreeNode(2)
    n2.left=n3


    print('---Start---')
    print n1.val
    r = object.getMinimumDifference(n1)
    print(r)
    print('---End---')
