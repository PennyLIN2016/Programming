# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # my own solution : 40 / 75 test cases passed. donot pass the tilt by recursion , should be saved by a static variable.
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        tilt= abs(self.findNext(root.left)[0]-self.findNext(root.right)[0])

        return tilt+self.findNext(root.left)[1]+self.findNext(root.right)[1]

    def findNext(self,node):
        if not node: return [0,0]
        sum= node.val+ self.findNext(node.left)[0]+self.findNext(node.right)[0]
        sumT=abs(self.findNext(node.left)[0]-self.findNext(node.right)[0]) + self.findNext(node.left)[1]+self.findNext(node.right)[1]
        return [sum,sumT]


    def findTilt1(self, root):
        #Runtime: 48 ms, faster than 71.15% of Python online submissions for Binary Tree Tilt.
        #Memory Usage: 14.5 MB, less than 100.00% of Python online submissions for Binary Tree Tilt.
        # google solution : use a static variable to save the return parameter.
        self.sums=0
        self.postorder(root)
        return self.sums
    def postorder(self,node):
        if not node: return 0
        left= self.postorder(node.left)
        right=self.postorder(node.right)
        self.sums+=abs(left-right)
        return left+right+node.val

if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1=TreeNode(1)
    n2=TreeNode(2)
    n3=TreeNode(3)
    n1.left=n2
    n1.right=n3


    print('---Start---')
    print (n1.val)
    r = object.findTilt(n1)
    print(r)
    print('---End---')