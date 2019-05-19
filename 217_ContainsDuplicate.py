class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Runtime: 104 ms, faster than 59.05% of Python online submissions for Contains Duplicate.
        #Memory Usage: 17.2 MB, less than 53.97% of Python online submissions for Contains Duplicate.
        if not nums: return False
        copy_s = set()
        copy_s.update(nums)
        return ( not len(copy_s)==len(nums))




if __name__ == '__main__':

    t =  [1,2,3,1]
    print(t)
    object = Solution()
    r = object.containsDuplicate(t)

    print(r)
    print('---End---')

