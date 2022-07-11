class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Runtime: 1898 ms, faster than 48.59% of Python3 online submissions for Maximum Average Subarray I.
        # Memory Usage: 26.1 MB, less than 60.13% of Python3 online submissions for Maximum Average Subarray I.
        # time: o(n) space:o(k)
        res = sum(nums[:k])
        cur = res
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i-k]
            res = max(cur, res)
        return round(res/k, 5)


if __name__ == '__main__':

    obj = Solution()
    A = [1,12,-5,-6,50,3]
    B = 4
    print('input: {}'.format(A))
    r = obj.findMaxAverage(A, B)
    print('output: {}'.format(r))