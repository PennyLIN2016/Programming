class Solution(object):
    def findLength1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # timeout: 37 / 57 test cases passed.
        # time: o(m*n* min(m, n)) space: o(n)
        posDict = {}
        for i, v in enumerate(nums1):
            if v in posDict:
                posDict[v].append(i)
            else:
                posDict[v] = [i]
        res = 0
        for m in range(len(nums2)):
            if nums2[m] in posDict:
                for start in posDict[nums2[m]]:
                    l = 1
                    while m+l < len(nums2) and start+l < len(nums1) \
                            and nums2[m+l] == nums1[start+l]:
                        l += 1
                    print('nums2[m]: {} m: {} start: {}, l: {}'
                          .format(nums2[m], m, start, l))
                    res = max(res, l)
        return res

    def findLength(self, nums1, nums2):
        # Runtime: 4714 ms, faster than 25.70% of Python online submissions for Maximum Length of Repeated Subarray.
        # Memory Usage: 35 MB, less than 40.19% of Python online submissions for Maximum Length of Repeated Subarray.
        # dp solution: time: o(m*n) space: m*n
        m, n = len(nums1), len(nums2)
        res = 0
        # dp[i][j] the max length start from nums1[i] / nums2[j]
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = 0
                res = max(res, dp[i][j])
        return res





obj = Solution()
t1 = [1,2,3,2,1]

t2 = [3,2,1,4,7]

print(obj.findLength(t1, t2))
