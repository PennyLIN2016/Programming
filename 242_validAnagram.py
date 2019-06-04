class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #Runtime: 44 ms, faster than 72.69% of Python online submissions for Valid Anagram.
        #Memory Usage: 13.3 MB, less than 26.98% of Python online submissions for Valid Anagram.
        if not s and not t: return True
        if not s or not t:return False
        # .sort() can not sort the char.
        return sorted(s)==sorted(t)


if __name__ == '__main__':
    s = "rat"
    t = "car"
    p = Solution()
    print(p.isAnagram(s,t))