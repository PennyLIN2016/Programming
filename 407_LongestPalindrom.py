import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Runtime: 20 ms, faster than 79.62% of Python online submissions for Longest Palindrome.
        #Memory Usage: 11.9 MB, less than 12.50% of Python online submissions for Longest Palindrome.
        nums= dict(collections.Counter(s))
        flag=1
        res=0
        for v in nums:
            if flag and nums[v]%2!=0:
                res+=1
                flag=0
            res+=int(nums[v]/2)*2
        return res
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Runtime: 41 ms, faster than 21.54% of Python online submissions for Longest Palindrome.
        #Memory Usage: 13.4 MB, less than 87.79% of Python online submissions for Longest Palindrome.
        import collections
        c = collections.Counter(s)
        flag = 0
        res = 0
        for v in c.values():
            res += v
            if v%2 != 0:
                if flag ==0:
                    flag = 1
                else:
                    res -= 1
        return res

if __name__ == '__main__':
    object = Solution()
    num = "abccccdd"

    print(num)
    r = object.longestPalindrome(num)
    print(r)
    print('---End---')
