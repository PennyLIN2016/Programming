class Solution(object):
    def isPerfectSquare1(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #Runtime: 24 ms, faster than 31.06% of Python online submissions for Valid Perfect Square.
        #Memory Usage: 11.7 MB, less than 48.88% of Python online submissions for Valid Perfect Square.
        # brutal solution: time : o(lgn) space :o(1)
        i =1
        while i*i <=num:
            if i*i==num:
                return True
            i+=1
        return False
    def isPerfectSquare1(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #Runtime: 12 ms, faster than 95.46% of Python online submissions for Valid Perfect Square.
        #Memory Usage: 11.7 MB, less than 59.38% of Python online submissions for Valid Perfect Square.
        # binary solution:
        while l<=r:
            mid= int((l+r)/2)
            if mid* mid == num:
                return True
            elif mid*mid < num:
                l= mid+1
            else:
                r=mid-1
        return False



if __name__ == '__main__':
    k = Solution()
    x =5


    r = k.isPerfectSquare(x)
    print(r)
    print('---End---')
