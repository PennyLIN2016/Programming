import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # Runtime: 164 ms, faster than 46.14% of Python online submissions for Sum of Square Numbers.
        #Memory Usage: 13.4 MB, less than 44.44% of Python online submissions for Sum of Square Numbers.
        # notes: 0 is integer a /b can be the same number
        if c ==0: return True
        n= int(math.sqrt(c))
        for i in range(1,n+1):
            tmp= int(math.sqrt(c-i*i))
            print tmp
            if tmp**2==c-i**2: return True
        return False
##### python3
    def judgeSquareSum(self, c: int) -> bool:
        # Runtime: 646 ms, faster than 24.30% of Python3 online submissions for Sum of Square Numbers.
        # Memory Usage: 13.9 MB, less than 61.40% of Python3 online submissions for Sum of Square Numbers.
        # math solution: time: o(lgc) space: o(1)
        import math
        i = 0
        while i <= int(math.sqrt(c/2)):
            if int(math.sqrt(c - i**2)) ** 2 == c - i**2:
                return True
            i += 1
        return False




if __name__ == '__main__':
    object = Solution()
    n1=4


    print('---Start---')

    r = object.judgeSquareSum(n1)
    print(r)
    print('---End---')
