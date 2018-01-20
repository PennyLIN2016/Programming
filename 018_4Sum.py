
class question(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums)< 4:
            return []

        nums.sort()

        s = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
            # skip the duplicate triples
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                right = len(nums)-1
                left = j+1
                target_sub = target -nums[i]-nums[j]
                while left < right:
                    if nums[right]+nums[left]> target_sub:
                        right -=1
                    elif nums[right]+nums[left]< target_sub:
                        left += 1
                    else:
                        s.append([nums[i],nums[j],nums[left],nums[right]])
                        right -= 1
                        left += 1
                        while left< right and nums[right+1] == nums[right]:
                            right -= 1
                        while left< right and nums[left]== nums[left-1]:
                            left += 1
        return s



if __name__ == '__main__':

    inputs = [1, 0, -1, 0, -2, 2]

    k = question()
    print 'Input :', inputs
    r = k.fourSum(inputs,0)
    print  'Result : ',r



