class Solution(object):
    def canPartition1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #89 / 104 test cases passed.Status: Time Limit Exceeded
        # dfs solution:
        def findnext(target,left):
            if not left:
                return False
            if target in left:
                return True
            if target<min(left):
                return False
            for value in left:
                left.remove(value)
                if findnext(target-value,left):
                    return True
                left.add(value)
            return False

        if sum(nums)%2!=0: return False
        return findnext(sum(nums)>>1,nums)
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Runtime: 24 ms, faster than 97.34% of Python online submissions for Partition Equal Subset Sum.
        #Memory Usage: 11.9 MB, less than 75.00% of Python online submissions for Partition Equal Subset Sum.
        # dfs solution(others)
        def findnext(nums,index,target):
            for i in range(2):
                # the two target can skip some numbers, keep the current possible set . do not need to start for the start number to travel all possible.
                if target[i]>=nums[index]:
                    target[i]-=nums[index]
                    if target[i]==0 or findnext(nums,index+1,target): return True
                    target[i]+=nums[index]
            return False
        if sum(nums)%2!=0 or sum(nums)>>1 < max(nums): return False
        # more efficient starting from greater num
        nums.sort(reverse = True)
        target= [sum(nums)>>1]*2
        return findnext(nums,0,target)


if __name__ == '__main__':
    object = Solution()
    num = [1, 5, 11, 5,6,8,14,8]

    print(num)
    print('---Start---')
    r = object.canPartition(num)
    print(r)
    print('---End---')
