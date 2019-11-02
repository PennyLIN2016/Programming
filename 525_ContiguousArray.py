
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




if __name__ == '__main__':
    object = Solution()
    s = [0,1,1,0,1,1,1,0]


    print('---Start---')
    print s
    r = object.findMaxLength(s)
    print(r)
    print('---End---')
