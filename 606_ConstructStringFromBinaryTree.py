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


if __name__ == '__main__':
    object = Solution()
    n1= None


    print('---Start---')
    print (n1)
    r = object.tree2str(n1)
    print(r)
    print('---End---')