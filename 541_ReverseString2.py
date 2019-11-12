class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        #Runtime: 20 ms, faster than 69.37% of Python online submissions for Reverse String II.
        #Memory Usage: 12.1 MB, less than 55.56% of Python online submissions for Reverse String II.
        if not s or k<=1: return s
        tmpL=list(s)
        for i in range(0,len(tmpL),2*k):
            if len(tmpL)-i>=k:
                tmpL[i:i+k]=reversed(tmpL[i:i+k])
            else:
                tmpL[i:len(tmpL)]=reversed(tmpL[i:len(tmpL)])
        return "".join(tmpL)

if __name__ == '__main__':
    object = Solution()
    n1="abcdefg"
    k = 8


    print('---Start---')
    print n1
    r = object.reverseStr(n1,k)
    print(r)
    print('---End---')
