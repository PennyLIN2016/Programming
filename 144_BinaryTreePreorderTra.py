# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # my solution 36s
    def preorderTraversal(self, root):

        root_l = []
        r = []
        if not root:
            return r
        root_l.append([0,root])
        r.append(root.val)

        while root_l:
            if root_l[-1][0] == 0 and root_l[-1][1].left:
                r.append(root_l[-1][1].left.val)
                root_l[-1][0] = 1
                root_l.append([0,root_l[-1][1].left])
                continue
            elif root_l[-1][0]!= 2 and root_l[-1][1].right:
                r.append(root_l[-1][1].right.val)
                root_l[-1][0] = 2
                root_l.append([0,root_l[-1][1].right])
                continue
            else:
                root_l.pop()

        return r



if __name__ == '__main__':

    P1 = TreeNode(1)
    P2 = TreeNode(2)
    P3 = TreeNode(3)
    P4 = TreeNode(4)
    P5 = TreeNode(5)

    P1.left = P2
    P1.right = P3
    P3.left = P4
    P3.right = P5


    k = Solution()
    r = k.preorderTraversal(P1)
    print (r)


