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


if __name__ == '__main__':
    object = Solution()
    num = "abccccdd"

    print(num)
    r = object.longestPalindrome(num)
    print(r)
    print('---End---')
