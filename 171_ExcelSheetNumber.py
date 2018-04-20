class Solution(object):
    # my solution 44s
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = 0
        for i in range(len(s)):
                n = n*26 + ord(s[i])-ord('A')+1
        return n


if __name__ == '__main__':
    s = 'ABA'

    k = Solution()

    print (k.titleToNumber(s))