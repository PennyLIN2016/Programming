import collections
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #Runtime: 20 ms, faster than 83.98% of Python online submissions for Find the Difference.
        #Memory Usage: 11.7 MB, less than 69.94% of Python online submissions for Find the Difference.
        # no need to if not s or not t: s ='' is also a valid input
        # collections.Counter : time o(n)
        resCount = dict(collections.Counter(s))
        for v in t:
            if v in resCount and resCount[v]!=0:
                resCount[v]-=1
            else:
                return v
    def findTheDifference1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
        # c += Counter() : remove all zero/negetive elements
        left = (c2-c1) + collections.Counter()
        return left.keys()[0]


if __name__ == '__main__':
    object = Solution()
    k = ""
    t='a'
    r = object.findTheDifference(k,t)
    print(r)
    print('---End---')
