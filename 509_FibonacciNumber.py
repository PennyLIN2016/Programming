class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        #Runtime: 16 ms, faster than 76.09% of Python online submissions for Fibonacci Number.
        #Memory Usage: 11.6 MB, less than 78.26% of Python online submissions for Fibonacci Number.
        # time o(n) space: 0(1)
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
    
    def fib1(self, n: int) -> int:
        # Runtime: 1335 ms, faster than 5.00% of Python3 online submissions for Fibonacci Number.
        # Memory Usage: 14 MB, less than 9.85% of Python3 online submissions for Fibonacci Number.
        # force recursion solution: time: o(n) space: O(1)
        if n == 0 : return 0
        if n == 1 : return 1
        return self.fib(n-1) + self.fib(n-2)

    def fib(self, n: int) -> int:
        # Runtime: 49 ms, faster than 46.97% of Python3 online submissions for Fibonacci Number.
        # Memory Usage: 13.9 MB, less than 55.71% of Python3 online submissions for Fibonacci Number.
        # time: o(n) space: (n)
        if n == 0 : return 0
        if n == 1 : return 1
        f = [0] * (n+1)
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] +f[i-2]
        return f[n]


if __name__ == '__main__':
    object = Solution()
    A= 30

    print('---Start---')
    print A
    r = object.fib(A)
    print(r)
    print('---End---')
