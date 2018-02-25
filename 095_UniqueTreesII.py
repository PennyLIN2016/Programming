# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def subTree(start,end):
            r = []
            if start > end:
                # start may skip over the end directly, so herein  start == end will cause error.
                r.append(None)
                return r

            for i in xrange(start,(end+1)):
                left= subTree(start,i-1)
                right = subTree(i+1,end)
                for j in xrange(len(left)):
                    for k in xrange(len(right)):
                        root = TreeNode(i)
                        root.left = left[j]
                        root.right = right[k]
                        r.append(root)
            return r

        if n == 0:
            return []
        return  subTree(1,n)



if __name__ == '__main__':

    k = Solution()
    N = 0
    r = k.generateTrees(N)
    print len(r)





