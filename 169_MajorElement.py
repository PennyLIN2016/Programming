class Solution(object):
    # my solution 47s
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = int(len(nums)/2)
        return sorted(nums)[times]

if __name__ == '__main__':
    nums = [1,2,1,5,3,1,1,4,1]


    k = Solution()

    print (k.majorityElement(nums))