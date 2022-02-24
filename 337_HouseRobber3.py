# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Runtime: 32 ms, faster than 95.73% of Python online submissions for House Robber III.
        #Memory Usage: 15.9 MB, less than 71.96% of Python online submissions for House Robber III.
        # Recursion w/ memorization  solution: time o(n) space: o(n)
        def bestRobber(node):
            # return (max value for node root, max vlaue for left child root,
            # max vlaue for the right child root)
            if node == None: return 0, 0, 0
            l, ll, lr = bestRobber(node.left)
            r, rl, rr = bestRobber(node.right)
            # max value for robbing the node = node val + all grandchild node values
            return max(node.val+ ll+lr+rr+rl, l+r), l, r
        return bestRobber(root)[0]



if __name__ == '__main__':
    k = Solution()
    node1= TreeNode(3)
    node2= TreeNode(2)
    node3= TreeNode(3)
    node4= TreeNode(3)
    node5 = TreeNode(1)
    node1.left= node2
    node1.right= node3
    node2.right=node4
    node3.right=node5

    r = k.rob(node1)
    print(r)
    print('---End---')



