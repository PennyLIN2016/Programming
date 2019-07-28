class Solution(object):
    def isSubsequence1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ##Runtime: 220 ms, faster than 37.99% of Python online submissions for Is Subsequence.
        #Memory Usage: 18.7 MB, less than 98.26% of Python online submissions for Is Subsequence.
        # time : o(n) space : o(1)
        if not s: return True
        if not t: return False
        p1,p2=0,0
        while p2<len(t):
            if s[p1]==t[p2]:
                p1+=1
            if p1==len(s): return True
            p2+=1

        return False

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #Runtime: 96 ms, faster than 84.98% of Python online submissions for Is Subsequence.
        #Memory Usage: 19 MB, less than 51.30% of Python online submissions for Is Subsequence.

        import collections
        tmp= collections.deque(s)
        for v in t:
            if not tmp:return True
            if v==tmp[0]:
                tmp.popleft()
        return not tmp

if __name__ == '__main__':
    object = Solution()
    k = "axc"
    t = "ahbgdc"

    r = object.isSubsequence(k,t)
    print(r)
    print('---End---')
