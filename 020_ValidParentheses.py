class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp=[]
        dic= ['()','{}','[]']

        for i in xrange(len(s)):
            tmp.append(s[i])
            if len(tmp)>=2 and tmp[-2]+tmp[-1] in dic:
                tmp.pop()
                tmp.pop()
        if tmp == []:
            return True
        else:
            return False

if __name__ == '__main__':
    inputs ='()'
    print inputs
    k = Solution()

    r = k.isValid(inputs)
    print r




