class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 244 ms, faster than 75.52% of Python online submissions for Maximum Product of Three Numbers.
        #Memory Usage: 12.6 MB, less than 11.11% of Python online submissions for Maximum Product of Three Numbers.
        # assuming the len(nums)>=3
        # if not nums or len(nums)<3: return 0
        nums.sort()
        r1=nums[-1]*nums[-2]*nums[-3]
        r2=nums[-1]*nums[0]*nums[1]
        return max(r1,r2)



if __name__ == '__main__':
    object = Solution()
    n1=[1,4,3,2]


    print('---Start---')

    r = object.maximumProduct(n1)
    print(r)
    print('---End---')
