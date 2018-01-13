
class question(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums)< 3:
            print'the list is incorrect!'
            return None

        nums.sort()

        min_gap = float("inf")
        sum_r = 0
        for i in range(len(nums)):

            right = len(nums)-1
            left = i+1
            while left < right:
                tmp_sum = nums[right]+nums[left]+nums[i]
                if tmp_sum == target:
                    return target
                elif tmp_sum< target:
                    if abs(tmp_sum-target)<min_gap:
                        sum_r = tmp_sum
                        min_gap = abs(tmp_sum-target)
                    left += 1
                else:
                    if abs(tmp_sum-target)<min_gap:
                        sum_r = tmp_sum
                        min_gap = abs(tmp_sum-target)
                    right -= 1

        return sum_r

if __name__ == '__main__':

    inputs = [-1, 0, 1, 2, -1, -4]
    k = question()
    print 'Input :', inputs
    r = k.threeSumClosest(inputs,0)
    print  'Result : ',r



