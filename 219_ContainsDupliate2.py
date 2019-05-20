class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #Runtime: 80 ms, faster than 53.58% of Python online submissions for Contains Duplicate II.
        #Memory Usage: 16.7 MB, less than 23.06% of Python online submissions for Contains Duplicate II.
        if not nums or k==0: return False
        dic_map ={}
        for i in range(len(nums)):
            if nums[i] in dic_map and i - dic_map[nums[i]]<=k:
                return True
            else:
                dic_map[nums[i]]= i
        return False




if __name__ == '__main__':
    nums = [99,99]
    k = 2

    t = Solution()
    print(t.containsNearbyDuplicate(nums,k))