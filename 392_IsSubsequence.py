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
            if not s: return True
    def isSubsequence1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #Runtime: 16 ms, faster than 93.76% of Python online submissions for Is Subsequence.
        #Memory Usage: 13.6 MB, less than 48.81% of Python online submissions for Is Subsequence.
        if not s: return True
        if not t: return False
        ls, lt = len(s), len(t)
        pos1, pos2 = 0, 0
        while pos1 < ls and pos2 <lt:
            while pos2<lt and s[pos1]!= t[pos2]:
                pos2+=1
            if pos2 == lt: return False
            if pos1 == ls-1: return True
            pos1 += 1
            pos2 +=1
        return False

if __name__ == '__main__':
    object = Solution()
    k = "axc"
    t = "ahbgdc"

    r = object.isSubsequence(k,t)
    print(r)
    print('---End---')
