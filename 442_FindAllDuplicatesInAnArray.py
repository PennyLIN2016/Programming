class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Runtime: 332 ms, faster than 72.03% of Python online submissions for Find All Duplicates in an Array.
        #Memory Usage: 18.7 MB, less than 66.67% of Python online submissions for Find All Duplicates in an Array.
        # other`s solution: time: o(n) space: o(n)  no extra space
        if not nums: return []
        res=[]
        # use the existing nums to save the status.
        # the value in nums: origal value or - value
        # nums[i] : [1,n]   so nums[abs(value)-1]
        for value in nums:
            if nums[abs(value)-1]<0:
                res.append(abs(value))
            else:
                nums[abs(value)-1]*=-1
        return res


if __name__ == '__main__':
    object = Solution()
    num =  [4,3,2,7,8,2,3,1]
    #num="abab"
    #p="ab"

    print(num)
    print('---Start---')
    r = object.findDuplicates(num)
    print(r)
    print('---End---')
