import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #Runtime: 28 ms, faster than 51.36% of Python online submissions for Perfect Number.
        #Memory Usage: 12.1 MB, less than 25.00% of Python online submissions for Perfect Number.
        if num<=1:return False
        s=1
        for factor in range(2,int(math.sqrt(num)+1)):
            if num%factor==0:
                s+= factor+num/factor
        return s==num
    def checkPerfectNumber(self, num: int) -> bool:
        # Runtime: 45 ms, faster than 69.52% of Python3 online submissions for Perfect Number.
        # Memory Usage: 13.8 MB, less than 97.06% of Python3 online submissions for Perfect Number.
        # time: o(lgn) space: o(1) python3.9
        import math
        if num == 1: return False
        divs = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                divs += i + int(num/i)
                if divs > num:
                    return False
        return divs == num

if __name__ == '__main__':
    object = Solution()
    A= 28
    print('---Start---')
    print A
    r = object.checkPerfectNumber(A)
    print(r)
    print('---End---')
