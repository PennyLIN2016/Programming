# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Runtime: 12 ms, faster than 96.80% of Python online submissions for First Bad Version.
        #Memory Usage: 11.8 MB, less than 35.07% of Python online submissions for First Bad
        # BS: timeo(lgN)
        l,r = 1, n
        while l<r:
            cur = int((l+r)/2)
            if isBadVersion(cur):
                # the answer <= cur ,so should keep the cur in the range .
                r= cur
            else:
                # in this case.  the answer > cur. so donot  need to keep the cur in the range.
                l = cur+1
        # l=r
        return l


if __name__ == '__main__':
    s= 5

    p = Solution()
    print(p.firstBadVersion(s))