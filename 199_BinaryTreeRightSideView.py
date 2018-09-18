# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
## passed 96.60%
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        child_list = [root]
        r = []
        while len(child_list)!= 0:
            r.append(child_list[0].val)
            child_list = self.update_child(child_list)
        return r

    def update_child(self,list):
        r_l = []
        for i in range(len(list)):
            if list[i].right != None:
                r_l.append(list[i].right)
            if list[i].left != None:
                r_l.append(list[i].left)
        return r_l

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
    print(t.rightSideView(n1))