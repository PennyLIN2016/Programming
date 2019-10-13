class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        #Runtime: 16 ms, faster than 76.09% of Python online submissions for Fibonacci Number.
        #Memory Usage: 11.6 MB, less than 78.26% of Python online submissions for Fibonacci Number.
        if N==0:return 0
        if N==1:return 1
        f0=0
        f1=1
        while N>1:
            tmp=f0+f1
            f0=f1
            f1=tmp
            N-=1
        return f1

if __name__ == '__main__':
    object = Solution()
    A= 30

    print('---Start---')
    print A
    r = object.fib(A)
    print(r)
    print('---End---')
