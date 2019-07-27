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

if __name__ == '__main__':
    object = Solution()
    k = ""
    t='a'
    r = object.findTheDifference(k,t)
    print(r)
    print('---End---')
