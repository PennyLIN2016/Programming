class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        #Runtime: 20 ms, faster than 66.54% of Python online submissions for Summary Ranges.
        #Memory Usage: 12 MB, less than 5.14% of Python online submissions for Summary Ranges.
        if not nums: return[]
        start= nums[0]
        cur= nums[0]
        res=[]
        for i in range(1,len(nums)):
            if nums[i]==cur+1:
                cur+=1
                continue
            if cur==start:
                res.append(str(start))
            else:
                res.append(str(start)+"->"+str(cur))
            start= nums[i]
            cur = start
        if cur==start:
            res.append(str(start))
        else:
            res.append(str(start)+"->"+str(cur))
        return res


if __name__ == '__main__':

    s= []

    object = Solution()
    r = object.summaryRanges(s)

    print(r)
    print('---End---')

