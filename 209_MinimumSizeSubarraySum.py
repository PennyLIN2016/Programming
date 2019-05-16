class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 60 ms, faster than 54.65% of Python online submissions for Minimum Size Subarray Sum.
        #Memory Usage: 13.9 MB, less than 60.95% of Python online submissions for Minimum Size Subarray Sum.
        min_len = len(nums)+1
        sum = 0
        l = 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum>=s:
                min_len = min(i-l+1,min_len)
                sum -= nums[l]
                l+=1
        return  min_len if min_len!=len(nums)+1 else 0

if __name__ == '__main__':
    s = 7
    t = [2,3,1,2,4,3]

    print(t)
    k = Solution()
    r = k.minSubArrayLen(s,t)

    print(r)
    print('---End---')

