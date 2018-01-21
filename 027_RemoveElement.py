class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        pos = 0
        for i in xrange(len(nums)):
            if nums[i]==val:
                continue
            else:
                nums[pos] = nums[i]
                pos+=1

        return pos

if __name__ == '__main__':

    list = [1,2,8,2,4,6,8,8,10,1]
    print 'input list :',list, '  len is ',len(list)

    k = Solution()
    r = k.removeElement(list,8)

    print 'output list is ',list,'  len  is ',r





