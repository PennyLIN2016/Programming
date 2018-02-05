class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
           return 0

        left = 0
        right = x
        while right >= left:
            mid = (right+left)/2
            if mid*mid > x:
                right = mid-1
            elif mid*mid < x:
                left = mid +1
            else:
                return mid

        return right







if __name__ == '__main__':

    a = 227

    A = Solution()
    r = A.mySqrt(a)
    print 'Result:',r





