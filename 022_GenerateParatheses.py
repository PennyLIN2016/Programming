class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generateRest(n1,stack,r,Target_n):
            '''
            :type n1 :int : the number of '('s which have not be matched by ')'
            :type stack : list of Parentheses : the string have not been completed.
            :type Target_n: int : the number of target pairs
            :rtype r :List[str]:save the strings have been generated.
            '''
            if len(stack)== 2*Target_n:
                if n1 == 0:
                    r.append(''.join(stack))
                return

            if n1 < Target_n :
                stack.append('(')
                generateRest(n1+1,stack,r,Target_n)
                stack.pop()
            if n1> 0:
                stack.append(')')
                generateRest(n1-1,stack,r,Target_n)
                stack.pop()

        r_s = []
        stack = []
        generateRest(0,stack,r_s,n)
        return r_s

if __name__ == '__main__':

    n = raw_input('Please Input N:')
    k = Solution()
    print 'N :',n
    r = k.generateParenthesis(int(n))
    print r
    print '|'.join(r)







