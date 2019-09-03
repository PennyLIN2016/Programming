class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Runtime: 880 ms, faster than 14.28% of Python online submissions for Circular Array Loop.
        #Memory Usage: 11.8 MB, less than 50.00% of Python online submissions for Circular Array Loop.
        # time :o(n) space:o(1)
        # get the next index
        def nextpos(index,lists):
            return(index+lists[index])%len(lists)
        for i in range(len(nums)):
            slow=i
            fast=nextpos(slow,nums)
            # guarantee the same direction
            while nums[fast]*nums[i]>0 and nums[nextpos(fast,nums)]*nums[i]>0:
                if fast==slow:
                    if slow ==nextpos(slow,nums):
                        # the length is 1
                        break
                    return True
                # guarantee the time complexity is o(n)
                slow=nextpos(slow,nums)
                fast=nextpos(nextpos(fast,nums),nums)
        return False


if __name__ == '__main__':
    object = Solution()
    A=[2,-1,1,2,2]
    print('---Start---')
    r = object.circularArrayLoop(A)
    print(r)
    print('---End---')
