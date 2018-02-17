import math
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def sub_next(nums,k,sub_list,r):
            r.append(sub_list)
            for i in xrange(k,len(nums)):
                sub_next(nums,i+1,sub_list+[nums[i]],r)


        r = []
        sub_list =[]
        # 0 : the first index of item to be added into the sub_list
        sub_next(nums,0,sub_list,r)

        return  r


if __name__ == '__main__':

    imputs = [1,2,3]
    k = Solution()
    print 'input',imputs
    r = k.subsets(imputs)
    print  'result : ',r


