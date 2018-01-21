class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)< 2:
            return  len(nums)
        pos = 0
        for i in xrange(1, len(nums)):
            if nums[i]==nums[pos]:
                continue
            else:
                pos +=1
                nums[pos] = nums[i]

        return pos+1

if __name__ == '__main__':

    list = [1,2,2,4,6,8,8,10]
    print 'input list :',list, '  len is ',len(list)

    k = Solution()
    r = k.removeDuplicates(list)

    print 'output list is ',list,'  len  is ',r





