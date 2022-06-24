class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Runtime: 37 ms, faster than 40.95% of Python online submissions for Merge Sorted Array.
        # Memory Usage: 13.2 MB, less than 98.01% of Python online submissions for Merge Sorted Array.
        # time: o(n+m) space: o(1)
        # make sure nums1[:cur] = nums2[:p2] will not change nums1 length when m = 0
        if m == 0:
            nums1[:] = nums2[:]
            return
        if n == 0:
            return

        p1, p2, cur = m, n, 0
        while p1 > 0 or p2 > 0:
            if p1 == 0:
                nums1[:cur] = nums2[:p2]
                break
            if p2 == 0:
                break
            cur -= 1
            if nums1[p1-1] <= nums2[p2-1]:
                p2 -= 1
                nums1[cur] = nums2[p2]
            else:
                p1 -= 1
                nums1[cur] = nums1[p1]



obj = Solution()
t1 = [0]
t2 = 0
t3 = [1]
t4 = 1
print(obj.merge(t1, t2, t3, t4))
print(t1)