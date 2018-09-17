class Solution(object):
    # this solution can pass in my local,
    # in leetcode: wrong answer: Do not return anything, modify nums in-place instead(maybe the python version problem)
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.revers(nums, 0, len(nums) - k - 1)
        self.revers(nums, len(nums) - k, len(nums) - 1)
        self.revers(nums, 0, len(nums) - 1)

    def revers(self,l, pos1, pos2):
        while pos1 < pos2:
            l[pos1], l[pos2] = l[pos2], l[pos1]
            pos1 += 1
            pos2 -= 1
        return l
    # passed, 98.73%
    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        pos1 = 0
        pos2 = len(nums) - k - 1
        while pos1 < pos2:
            nums[pos1], nums[pos2] = nums[pos2], nums[pos1]
            pos1 += 1
            pos2 -= 1
        pos1 = len(nums) - k
        pos2 = len(nums) - 1
        while pos1 < pos2:
            nums[pos1], nums[pos2] = nums[pos2], nums[pos1]
            pos1 += 1
            pos2 -= 1
        pos1 = 0
        pos2 = len(nums) - 1
        while pos1 < pos2:
            nums[pos1], nums[pos2] = nums[pos2], nums[pos1]
            pos1 += 1
            pos2 -= 1
    # passed
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        old_nums = nums[:]
        for i in xrange(len(nums)):
            nums[(i + k) % len(nums)] = old_nums[i]

if __name__ == '__main__':

    s = [1,2,3,4,5,6,7]
    n = 3

    t = Solution()
    t.rotate(s, n)

    print(s)