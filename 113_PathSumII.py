#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def nextsum(root,target,path_r,path):
            if (root.left== None ) and (root.right== None) and target == root.val:
                path.append(root.val)
                tmp = path[:]
                path_r.append(tmp)
                #  or path_r.append(path+[]) otherwise, use path_r.append(path), when the path changed , the values in
                # path_r also be changed.
                path.pop()
                return
            if (root.left== None ) and (root.right== None) and target != root.val:
                return

            if root.left:
                path.append(root.val)
                nextsum(root.left,target-root.val,path_r,path)
                path.pop()
            if root.right:
                path.append(root.val)
                nextsum(root.right,target-root.val,path_r,path)
                path.pop()


        if not root:
            return []
        path_r = []
        nextsum(root,sum,path_r,[])
        return path_r




if __name__ == '__main__':
    root = TreeNode(10)
    left = TreeNode(21)
    right = TreeNode(15)
    left_1 = TreeNode(6)
    left_2 = TreeNode(20)
    root.left= left
    root.right = right
    right.left = left_1
    right.right = left_2

    sum = 31

    k = Solution()
    r = k.hasPathSum(root,sum)
    print r
