
class question(object):# low efficiency but can return the longest string, not just the length.
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2 :
            return len(nums)
        dict = {}
        pos = 0
        for i in xrange(len(nums)):
            if dict.has_key(nums[i]):
                if dict[nums[i]] < 2:
                    dict[nums[i]] += 1
                    nums[pos] = nums[i]
                    pos += 1
            else:
                dict[nums[i]] = 1
                nums[pos] = nums[i]
                pos += 1

        return pos


if __name__ == '__main__':

    inputs = [1,1,1,2,2,3]
    k = question()
    r = k.removeDuplicates(inputs)
    print  'result : Length :',r,' --',inputs[:r]


