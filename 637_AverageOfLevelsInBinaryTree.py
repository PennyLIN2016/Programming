# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # Runtime: 48 ms, faster than 75.70% of Python3 online submissions for Average of Levels in Binary Tree.
        # Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Average of Levels in Binary Tree.
        # bfs solution: t(n)= O(m): m : the number of node s(n)=o(n)
        if not root: return []
        res=[]
        stack=[root]
        while stack:
            sum=0
            tmp=[]
            for value in stack:
                print (value.val)
                sum+=value.val
                if value.left: tmp.append(value.left)
                if value.right:tmp.append(value.right)
            # in python 2, res.append(sum/float(len(stack)))
            res.append(sum/len(stack))
            stack=tmp
            print (res)
        return res

### python 3

    def averageOfLevels(self, root: TreeNode) -> list[float]:
        # Runtime: 94 ms, faster than 21.40% of Python3 online submissions for Average of Levels in Binary Tree.
        # Memory Usage: 16.5 MB, less than 47.63% of Python3 online submissions for Average of Levels in Binary Tree.
        # time: o(n: nodes) space: o(n)
        if not root: return []
        res = []
        nodes = [root]

        while nodes:
            sumVal = 0
            tmp = []
            for v in nodes:
                sumVal += v.val
                if v.left: tmp.append(v.left)
                if v.right: tmp.append(v.right)
            res.append(round(sumVal / len(nodes), 5))
            nodes = tmp

        return res




if __name__ == '__main__':
    object = Solution()
    n1=TreeNode(3)
    n2=TreeNode(9)
    n3=TreeNode(20)
    n1.left=n2
    n1.right=n3
    n4=TreeNode(15)
    n5=TreeNode(7)
    n3.left=n4
    n3.right=n5


    print('---Start---')
    print (n1)
    r = object.averageOfLevels(n1)
    print(r)
    print('---End---')
