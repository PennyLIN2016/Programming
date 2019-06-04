class Solution(object):
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Runtime: 52 ms, faster than 40.82% of Python online submissions for Single Number III.
        # Memory Usage: 13.8 MB, less than 35.27% of Python online submissions for Single Number III.
        # runtime: o(len(nums))  spece(o(n/2))
        if not nums: return []
        one_set =set()
        for value in nums:
            if value in one_set:
                one_set.discard(value)
            else:
                one_set.add(value)
        return list(one_set)

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Runtime: 52 ms, faster than 40.82% of Python online submissions for Single Number III.
        #Memory Usage: 13 MB, less than 90.63% of Python online submissions for Single Number III.
        # runtime: o(len(nums)) space : len(res)=2 + pre
        if not nums: return []
        if len(nums)==1: return nums
        if len(nums)==2:
            if nums[0]==nums[1]:
                return []
            else:
                return nums
        res=[]
        nums.sort()
        pre=nums[0]+1
        for i in range(len(nums)-1):

            if nums[i]!=pre and nums[i]!=nums[i+1]:
                res.append(nums[i])
            if len(res)==2:
                break
            pre=nums[i]
        if len(res)<=1:
            res.append(nums[-1])
        return res

    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Runtime: 48 ms, faster than 60.45% of Python online submissions for Single Number III.
        # Memory Usage: 14.8 MB, less than 7.14% of Python online submissions for Single Number
        #runtime: o(len(nums)/2) space: len(res) = 2 + counter(n/2)
        import collections
        res=[]
        count_nums= collections.Counter(nums)
        for value,time in count_nums.items():
            if time==1:
                res.append(value)
        return res


    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Runtime: 48 ms, faster than 60.45% of Python online submissions for Single Number III.
        # Memory Usage: 14.8 MB, less than 7.14% of Python online submissions for Single Number
        #runtime: o(n) space:constant
        # any number  ^ 0 equals to itself. two same number ^ , the result is 0.
        r_or = 0
        # get the two different numbers result of ^
        for value in nums:
            r_or ^= value
        mask=1
        # r_or & mask ==0 means the "1" bits in mask is 0 in r_or, and then the two different numbers in that bit are the same.
        # use the loop to find the rightest "1" in r_or
        while r_or & mask ==0:
            mask=mask<<1
        # mask holds the one different bit pos in the two different numbers:
        num1,num2=0,0
        for value in nums:
            if value & mask ==0:
                # '0' in the special bit in value
                # the same numbers will get offset each other and just leave the value of one different number
                num1^=value
            else:
                num2^=value
        return [num1,num2]



if __name__ == '__main__':
    s= [1,2,1,3,2,5]
    p = Solution()
    print(p.singleNumber(s))