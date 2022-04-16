class Solution(object):
    def repeatedSubstringPattern1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # timeout: 116/120 passed
        # time: o(n*n)
        substr=''
        for i in range(int(len(s)/2)):
            substr+=s[i]
            if ''.join(s.split(substr))=='':return True
        return False

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Runtime: 16 ms, faster than 94.07% of Python online submissions for Repeated Substring Pattern.
        #Memory Usage: 12.1 MB, less than 75.00% of Python online submissions for Repeated Substring Pattern.

        #remove the first and last char
        doubleS= (s+s)[1:-1]
        print doubleS

        # s is made of repeated subs, so broken the the first and the last subs.
        # in double s, at least one whole s can be found.
        # cannot find the s
        return doubleS.find(s)!=-1
    
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Runtime: 76 ms, faster than 58.49% of Python online submissions for Repeated Substring Pattern.
        # Memory Usage: 14 MB, less than 32.80% of Python online submissions for Repeated Substring Pattern.
        # brutal solution:
        # time: 0(n**2) time: o(n)
        l = len(s)
        for i in range(1, l//2+1):
            if l % i != 0:
                continue
            tmp = s[0:i]
            if ''.join((s.split(tmp))) == '':
                return True
        return False


if __name__ == '__main__':
    object = Solution()
    A= "abcabcabcabc"
    print('---Start---')
    r = object.repeatedSubstringPattern(A)
    print(r)
    print('---End---')
