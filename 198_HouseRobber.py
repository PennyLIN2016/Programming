class Solution(object):
    #passed 99.96
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_list = [0 for i in range(len(nums)+1)]

        for j in range(len(nums)):
            if j == 0:
                num_list[j+1] = nums[j]
                continue
            num_list[j+1]= max(num_list[j-1]+nums[j],num_list[j])

        return num_list[-1]

if __name__ == '__main__':

    s = [1,2,3,1]

    t = Solution()


    print(t.rob(s))