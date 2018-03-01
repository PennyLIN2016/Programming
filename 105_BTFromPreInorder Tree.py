# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder \
            or len(preorder)== 0 or len(inorder) == 0:
         return None
        self.pos = 0
        return self.next_build(preorder,inorder)

    def next_build(self,l1,l2):
        root = TreeNode(l1[self.pos])
        p = l2.index(l1[self.pos])
        if p > 0:
            self.pos += 1
            root.left = self.next_build(l1,l2[0:p])
        if p < len(l2)-1:
            self.pos += 1
            root.right = self.next_build(l1,l2[p+1:])
        return root



if __name__ == '__main__':
    l1 = [3,9,20,15,7]
    l2 =  [9,3,15,20,7]
    k = Solution()
    r = k.buildTree(l1,l2)
    print r





