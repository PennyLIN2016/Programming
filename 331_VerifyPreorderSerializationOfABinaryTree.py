class Solution(object):
    def isValidSerialization1(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        #Runtime: 20 ms, faster than 93.37% of Python online submissions for Verify Preorder Serialization of a Binary Tree.
        #Memory Usage: 11.9 MB, less than 28.57% of Python online submissions for Verify Preorder Serialization of a Binary Tree.
        # stack and cut leaves solution:time: o(n) space: o(n)
        stack = []
        for value in preorder.split(','):
            stack.append(value)
            while len(stack)>=3 and stack[-2:]==['#','#'] and stack[-3]!='#':
                stack=stack[:-3]+['#']
        return len(stack)==1 and stack[0]=='#'

    def isValidSerialization2(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        ##Runtime: 16 ms, faster than 98.72% of Python online submissions for Verify Preorder Serialization of a Binary Tree.
        #Memory Usage: 11.8 MB, less than 62.19% of Python online submissions for Verify Preorder Serialization of a Binary Tree.
        # time : o(n) space : o(1)
        #In a binary tree, if we consider null as leaves, then
        #all non-null node provides 2 outdegree and 1 indegree (2 children and 1 parent), except root
        #all null node provides 0 outdegree and 1 indegree (0 child and 1 parent).

        #Suppose we try to build this tree. During building, we record the difference between out degree and in degree diff = outdegree - indegree.
        #for a preordr, the root always is in front of children. so the diff should be >=0. 0 only happens when finished.When the next node comes, we then #decrease diff by 1, because the node provides an in degree. If the node is not null, we increase diff by2, because it provides two out degrees.
        #If a serialization is correct, diff should never be negative and diff will be zero when finished.

        if not preorder: True
        diff= 1# for the root node
        for value in preorder.split(','):
            diff-=1 # for one parent
            if diff<0: return False
            if value!='#':
                diff+=2# for 2 children

        return diff==0
    
   def isValidSerialization3(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # save the nodes have not be cut off by a sub tree.
        stack = []
        for v in preorder.split(','):
            stack.append(v)
            # stack[-2:] == ['#', '#'] : the front node is one root of sub tree.
            while len(stack)>= 3 and stack[-2:] == ['#', '#']:
                # if the root is '#' -- False
                if stack[-3] != '#': return False
                # cut the sub tree and add a leave node
                stack = stack[:-3] + ['#']
        # the last stack should be the root 
        return len(stack) == 1 and stack[0] == '#'


if __name__ == '__main__':
    import sys
    k = Solution()
    l= "1,#,#,#,#"

    r = k.isValidSerialization(l)
    print(r)
    print('---End---')



