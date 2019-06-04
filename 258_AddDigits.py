class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Runtime: 20 ms, faster than 91.40% of Python online submissions for Add Digits.
        # Memory Usage: 11.7 MB, less than 62.85% of Python online submissions for Add Digits.
        while num >=10:
            tmp = str(num)
            num= 0
            for char in tmp:
                num+= int(char)
        return num

if __name__ == '__main__':
    s = 25698
    p = Solution()
    print(p.addDigits(s))