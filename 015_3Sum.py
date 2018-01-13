
class question(object):

    def threeSum(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)< 3:
            return []

        nums.sort()
        if nums[0]> 0 or nums[-1]< 0:
            return []

        s = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
            # skip the duplicate triples
                continue
            right = len(nums)-1
            left = i+1
            while left < right:
                if nums[right]+nums[left]+nums[i]> 0:
                    right -=1
                elif nums[right]+nums[left]+nums[i]<0:
                    left += 1
                else:
                    s.append([nums[i],nums[left],nums[right]])
                    right -= 1
                    left += 1
                    while left< right and nums[right+1] == nums[right]:
                        right -= 1
                    while left< right and nums[left]== nums[left-1]:
                        left += 1
        return s



if __name__ == '__main__':

    inputs = [-1, 0, 1, 2, -1, -4]
    k = question()
    print 'Input :', inputs
    r = k.threeSum(inputs)
    print  'Result : ',r



