class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        #Runtime: 36 ms, faster than 75.58% of Python online submissions for Contains Duplicate III.
        #Memory Usage: 13.6 MB, less than 97.91% of Python online submissions for Contains Duplicate III.

        # when t==0, no duplicated nums can return false directly.
        if t==0 and len(nums)==len(set(nums)):
            return False
        for i in range(len(nums)):
            for j in range(1,k+1):
                if (i+j)>= len(nums):
                    break
                if abs(nums[i+j]-nums[i])<=t:
                    return True
        return False



if __name__ == '__main__':
    nums = [1,0,1,1]
    k = 2
    l =3

    p = Solution()
    print(p.containsNearbyAlmostDuplicate(nums,k,l))