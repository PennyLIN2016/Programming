class Solution(object):
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ##Runtime: 96 ms, faster than 17.38% of Python online submissions for Move Zeroes.
        #Memory Usage: 12.9 MB, less than 16.13% of Python online submissions for Move Zeroes.
        # Time O(n) space: constant
        countZero= 0
        i=0
        cur_l= len(nums)
        while i <cur_l:
            if nums[i]==0:
                countZero+=1
                cur_l-=1
                nums[i:cur_l]=nums[i+1:cur_l+1]
            else:
                i+=1
        for j in range(countZero):
            nums[cur_l+j]= 0
        return nums

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #Runtime: 40 ms, faster than 65.35% of Python online submissions for Move Zeroes.
        #Memory Usage: 12.8 MB, less than 41.58% of Python online submissions for Move Zeroes.
        # Time O(n) space: constant
        Counter= 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[Counter]=nums[i]
                Counter+=1
        while Counter< len(nums):
            nums[Counter]= 0
            Counter +=1
        return nums

if __name__ == '__main__':

    s= [0,1,0,3,12]

    object = Solution()
    r = object.moveZeroes(s)

    print(r)
    print('---End---')

