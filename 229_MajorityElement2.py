class Solution(object):
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Runtime: 100 ms, faster than 63.54% of Python online submissions for Majority Element II.
        #Memory Usage: 12.9 MB, less than 35.65% of Python online submissions for Majority Element II.
        if not nums: return []
        res=[]
        nums.sort()
        i=0
        while i< len(nums) :
            j=i+1
            while j<len(nums):
                if nums[i]==nums[j]:
                    j+=1
                else:
                    break
            if (j-i) > int(len(nums)/3):
                res.append(nums[i])
            i=j
        return res
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import collections
        #Runtime: 108 ms, faster than 46.21% of Python online submissions for Majority Element II.
        #Memory Usage: 12.8 MB, less than 85.88% of Python online submissions for Majority Element II.
        N = len(nums)
        count = collections.Counter(nums)
        res = []
        for n, t in count.items():
            if t > N / 3:
                res.append(n)
        return res



if __name__ == '__main__':

    s= [1]

    object = Solution()
    r = object.majorityElement(s)

    print(r)
    print('---End---')

