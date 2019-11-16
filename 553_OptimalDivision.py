class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        #Runtime: 16 ms, faster than 74.62% of Python online submissions for Optimal Division.
        #Memory Usage: 11.9 MB, less than 50.00% of Python online submissions for Optimal Division.
        #google solution: time:0(n) space:o(1)

        nums=map(str,nums)
        if len(nums)<=2: return "/".join(nums)
        return nums[0]+'/('+"/".join(nums[1:])+')'

if __name__ == '__main__':
    object = Solution()
    #n1= [1000,100,10,2]
    n1=[1000,100,10]

    print('---Start---')
    print n1
    r = object.optimalDivision(n1)
    print(r)
    print('---End---')
