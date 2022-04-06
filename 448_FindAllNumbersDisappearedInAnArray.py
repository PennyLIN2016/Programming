class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Runtime: 332 ms, faster than 64.73% of Python online submissions for Find All Numbers Disappeared in an Array.
        #Memory Usage: 19 MB, less than 88.46% of Python online submissions for Find All Numbers Disappeared in an Array.
        for v in nums:
            if nums[abs(v)-1]>0:
                nums[abs(v)-1]*=-1
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:res.append(i+1)
        return res
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Runtime: 403 ms, faster than 48.50% of Python online submissions for Find All Numbers Disappeared in an Array.
        # Memory Usage: 20.5 MB, less than 94.99% of Python online submissions for Find All Numbers Disappeared in an Array.
        # time: o(n) space o(1)
        res = []
        n = len(nums)
        for v in nums:
            cur = abs(v)
            nums[cur-1] = abs(nums[cur-1]) * -1

        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res

if __name__ == '__main__':
    object = Solution()
    num =  [4,3,2,7,8,2,3,1]



    print(num)
    print('---Start---')
    r = object.findDisappearedNumbers(num)
    print(r)
    print('---End---')
