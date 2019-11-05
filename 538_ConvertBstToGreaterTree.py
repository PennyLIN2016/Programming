# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def convertBST1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 211 / 212 test cases passed. timeout
        self.map={}
        def GetSumMap(root):
            if not root:
                return
            GetSumMap(root.left)
            if root.val  not in self.map:
                self.map[root.val]=0
            for key in self.map:
                if key<root.val: self.map[key]+=root.val
            GetSumMap(root.right)

        def GetCon(root):
            if not root:
                return
            root.val+=self.map[root.val]
            GetCon(root.left)
            GetCon(root.right)


        GetSumMap(root)
        print self.map
        GetCon(root)
        return root

    def convertBST2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #time out : 211 / 212 test cases passed.
        self.visited=set()
        def GetSum(root):
            if not root:
                return

            GetSum(root.right)
            tmp=0
            for key in self.visited:
                if key>root.val: tmp+=key
            if root.val not in self.visited:
                self.visited.add(root.val)
            root.val+=tmp
            GetSum(root.left)
            print(self.visited)

        GetSum(root)
        print(self.visited)
        return root

    def convertBST2(self, root):
        #Runtime: 64 ms, faster than 52.46% of Python online submissions for Convert BST to Greater Tree.
        # Memory Usage: 16.3 MB, less than 19.05% of Python online submissions for Convert BST to Greater Tree
        # question: what happens when there are duplicates
        self.sum=0
        def getSum(root):
            if not root:return
            getSum(root.right)
            self.sum+=root.val
            root.val=self.sum
            getSum(root.left)
        getSum(root)
        return root




if __name__ == '__main__':
    object = Solution()
    n1=TreeNode(5)
    n2=TreeNode(2)
    n1.left=n2
    n3=TreeNode(13)
    n1.right=n3
    n4=TreeNode(3)
    n2.right=n4


    print('---Start---')
    print n1.val
    r = object.convertBST(n1)
    print(r.val)
    print('---End---')
