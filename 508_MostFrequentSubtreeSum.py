import collections
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #Runtime: 40 ms, faster than 70.48% of Python online submissions for Most Frequent Subtree Sum.
        #Memory Usage: 17.9 MB, less than 50.00% of Python online submissions for Most Frequent Subtree Sum.
        if not root: return []
        res=[]
        fre_dic= collections.defaultdict(int)
        self.sumSubtree(root,fre_dic)
        max_f=max(fre_dic.values())
        for value in fre_dic:
            if fre_dic[value]==max_f:
                res.append(value)
        return res

    def sumSubtree(self,root,freq):
        if not root:
            return 0
        tmp= root.val+self.sumSubtree(root.right,freq)+self.sumSubtree(root.left,freq)
        freq[tmp]+=1
        return tmp
    # Runtime: 62 ms, faster than 65.38% of Python3 online submissions for Most Frequent Subtree Sum.
    # Memory Usage: 17.4 MB, less than 76.12% of Python3 online submissions for Most Frequent Subtree Sum.
    # time: o(n) space: o(n)
    def findFrequentTreeSum(self, root: TreeNode) -> list[int]:
        def getSum(node):
            if not node:
                return 0
            res = node.val
            if node.left:
                res += getSum(node.left)
            if node.right:
                res += getSum(node.right)
            freDict[res] += 1
            return res
        if not root: return []
        freDict = collections.defaultdict(int)
        getSum(root)
        target = max(freDict.values())
        ans = []
        for k, v in freDict.items():
            if v == target:
                ans.append(k)
        return ans

if __name__ == '__main__':
    object = Solution()
    A= TreeNode(5)
    n1=TreeNode(2)
    n2=TreeNode(-5)
    A.left=n1
    A.right=n2
    print('---Start---')
    print A.val
    r = object.findFrequentTreeSum(A)
    print(r)
    print('---End---')
