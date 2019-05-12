class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #Runtime: 20 ms, faster than 99.81% of Python online submissions for Isomorphic Strings.
        #Memory Usage: 14.6 MB, less than 5.00% of Python online submissions for Isomorphic Strings.
        return(len(set(s))==len(set(t))==len(set(zip(s,t))))

if __name__ == '__main__':
    s = "egg"
    t = "adt"

    k = Solution()
    r = k.isIsomorphic(s,t)

    print(r)
    print('---End---')

