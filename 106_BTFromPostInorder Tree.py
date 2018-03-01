# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution(object):


    def buildTree(self,inorder,postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not postorder or not inorder \
            or len(postorder)== 0 or len(inorder) == 0:
         return None
        self.pos = len(postorder)-1
        return self.next_build(inorder,postorder)

    def next_build(self,l1,l2):
        root = TreeNode(l2[self.pos])
        p = l1.index(l2[self.pos])
        if p < len(l1)-1:
            self.pos -= 1
            root.right = self.next_build(l1[p+1:],l2)
        if p > 0:
            self.pos -= 1
            root.left = self.next_build(l1[0:p],l2)

        return root


if __name__ == '__main__':
    l1 = [9,3,15,20,7]
    l2 =  [9,15,7,20,3]
    k = Solution()
    r = k.buildTree(l1,l2)
    print r





