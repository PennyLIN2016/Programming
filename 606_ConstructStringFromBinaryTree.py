# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def tree2str1(self, t: TreeNode) -> str:
        # Runtime: 52 ms, faster than 83.07% of Python3 online submissions for Construct String from Binary Tree.
        # Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Construct String from Binary Tree.
        # recursion solution: t(n)= o(n) s(n)= o(n)
        if not t: return ''
        left= '({})'.format(self.tree2str(t.left)) if t.left or t.right else ''
        right= '({})'.format(self.tree2str(t.right)) if t.right else ''
        return '{}{}{}'.format(t.val,left,right)
     
  #############python3
    def tree2str(self, root: TreeNode) -> str:
        # Runtime: 62 ms, faster than 71.27% of Python3 online submissions for Construct String from Binary Tree.
        # Memory Usage: 16.8 MB, less than 5.70% of Python3 online submissions for Construct String from Binary Tree.
        # time: o(n) space: o(n)
        if not root:
            return ""
        s1 = self.tree2str(root.left)
        s2 = self.tree2str(root.right)
        res = str(root.val)
        # if s1= '' and s2 != '' need to add () to mean there is an empty left tree
        if s1 or s2: res += '({})'.format(s1)
        if s2 != '': res += '({})'.format(s2)
        return res



if __name__ == '__main__':
    object = Solution()
    n1= None


    print('---Start---')
    print (n1)
    r = object.tree2str(n1)
    print(r)
    print('---End---')
