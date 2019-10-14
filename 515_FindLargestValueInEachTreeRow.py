# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #Runtime: 32 ms, faster than 89.66% of Python online submissions for Find Largest Value in Each Tree Row.
        #Memory Usage: 16.3 MB, less than 33.33% of Python online submissions for Find Largest Value in Each Tree Row.
        if not root: return []
        s=[root]
        res=[root.val]
        while s:
            tmp=[]
            cur=float('-inf')
            for value in s:
                if value.left:
                    tmp.append(value.left)
                    cur=max(cur,value.left.val)
                if value.right:
                    tmp.append(value.right)
                    cur=max(cur,value.right.val)
            if tmp:
                res.append(cur)
            s=tmp
        return res


if __name__ == '__main__':
    object = Solution()
    A= TreeNode(2)
    n1=TreeNode(1)
    n2=TreeNode(3)
    A.left=n1
    A.right=n2
    print('---Start---')
    print A.val
    r = object.largestValues(A)
    print(r)
    print('---End---')
