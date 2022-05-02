class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 308 ms, faster than 97.76% of Python online submissions for Max Consecutive Ones.
        #Memory Usage: 11.9 MB, less than 68.42% of Python online submissions for Max Consecutive Ones.
        res=0
        l=0
        for value in nums:
            if value:
                l+=1
            else:
                res=max(l,res)
                l=0
        
        return max(l,res)


if __name__ == '__main__':
    object = Solution()
    A= [0,0,1,]

    print('---Start---')
    r = object.findMaxConsecutiveOnes(A)
    print(r)
    print('---End---')
