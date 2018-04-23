# Definition for a  binary tree node
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class BSTIterator(object):
    # my solution 99s
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.r = []
        while root:
            self.r.append(root)
            root = root.left


    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.r) > 0

    def next(self):
        """
        :rtype: int
        """
        tmp_node = self.r.pop()

        if tmp_node.right:
            tmp = tmp_node.right
            self.r.append(tmp)
            while tmp.left:
                self.r.append(tmp.left)
                tmp = tmp.left

        return tmp_node.val

if __name__ == '__main__':

        p1 = TreeNode(4)
        p2 = TreeNode(0)
        p3 = TreeNode(6)
        p4 = TreeNode(2)
        p5 = TreeNode(4)
        p6 = TreeNode(7)
        p7 = TreeNode(1)
        p8 = TreeNode(3)
        p1.left = p2
        p1.right = p3
        p2.right = p4
        p3.left = p5
        p3.right = p6
        p4.left = p7
        p4.right = p8


        k = BSTIterator(p1)

        print('the order is:',end='')
        while k.hasNext():
            print('%i '%(k.next()),end='')
        print





