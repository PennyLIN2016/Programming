
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 796 ms, faster than 75.18% of Python online submissions for Contiguous Array.
        #Memory Usage: 15.4 MB, less than 100.00% of Python online submissions for Contiguous Array.
        # dp solution : time complexity o(n) space complexity o(n)
        if not nums or len(nums)<2: return 0
        # keep the first index for specific curSum
        dmap={}
        res=0
        # curSum : the sum of [:i+1]
        curSum=0
        for i,value in enumerate(nums):
            curSum+=value if value else -1
            if curSum==0:
                # the current longest substr 0..i
                res=i+1
            # look for the same curSum
            elif curSum in dmap:
                res = max(res,i-dmap[curSum])
            else:
                dmap[curSum]=i
        return res

    def findMaxLength(self, nums: list[int]) -> int:
        # timeout: 25 / 564 test cases passed.
        for i, v in enumerate(nums):
            if v == 0:
                nums[i] = -1
        res = 0
        for i in range(len(nums), -1, -1):
            for j in range(i, len(nums)):
                print('i: {} j: {}'.format(i, j))
                if i == j:
                    continue
                if sum(nums[i:j+1]) == 0:
                    res = max(j-i+1, res)
        return res

    def findMaxLength(self, nums: list[int]) -> int:
        # Runtime: 886 ms, faster than 87.29% of Python3 online submissions for Contiguous Array.
        # Memory Usage: 19.5 MB, less than 40.04% of Python3 online submissions for Contiguous Array.
        # similar solution to question 523
        # time: o(n) space: o(n)
        res = 0
        count = 0
        # dicLen[i] the extre 1 of nums[:i+1]
        dicLen = {0: 0}
        for i, v in enumerate(nums, 1):
            count += 1 if v == 1 else -1
            # Match the subArray:[:i+1] - [:k] dicLen(count) = k
            if count in dicLen:
                res = max(res, i - dicLen[count])
            else:
                dicLen[count] = i
        return res


if __name__ == '__main__':
    object = Solution()
    s = [0,1,1,0,1,1,1,0]


    print('---Start---')
    print s
    r = object.findMaxLength(s)
    print(r)
    print('---End---')
