# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]

        """
        # Runtime: 20 ms, faster than 90.94% of Python online submissions for Binary Tree Paths.
        # Memory Usage: 11.9 MB, less than 30.07% of Python online submissions for Binary Tree
        # dfs iteration to get the leaf and path to save the str
        def nextStep(root,path,leaf_path):
            if root.left==None and root.right==None:
                leaf_path.append(path+str(root.val))
                return
            if root.left!=None:
                nextStep(root.left,path+str(root.val)+'->',leaf_path)
            if root.right!=None:
                nextStep(root.right, path + str(root.val)+'->', leaf_path)

        if not root: return []
        leafs=[]
        nextStep(root,'',leafs)
        return leafs

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    n1.left = n2
    n1.right = n3
    n2.right = n5
    n3.right = n4

    t = Solution()
    print(t.binaryTreePaths(n1))