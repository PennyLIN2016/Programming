class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        #Runtime: 12 ms, faster than 96.38% of Python online submissions for Word Pattern.
        #Memory Usage: 11.9 MB, less than 13.79% of Python online submissions for Word Pattern.
        #time split: O(n) zip: O(1)space (n)
        if not pattern and not str : return  True
        if not pattern or not str: return False
        words=str.split()
        if len(words)!=len(pattern):return False
        return len(set(words))==len(set(pattern))==len(set(zip(pattern,words)))


if __name__ == '__main__':
    k = Solution()
    s = "abba"
    t = "dog cat cat dog"
    r = k.wordPattern(s,t)

    print(r)
    print('---End---')



