class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        # Runtime: 284 ms, faster than 61.23% of Python3 online submissions for Set Mismatch.
        # Memory Usage: 15.3 MB, less than 81.04% of Python3 online submissions for Set Mismatch.
        # time: o(n) space: 0(1)
        exist = 0
        repeated = 0
        for v in nums:
            pos = 1 << (v-1)
            if exist & pos != 0:
                repeated = v
            else:
                exist |= pos
            print('exist: {} pos: {} repeated: {}'.format(bin(exist), bin(pos), repeated))
        n = 1
        while n <= len(nums):
            if exist & (1<<(n-1)) == 0:
                return [repeated, n]
            n += 1
            print('2-exist: {} n: {}'.format(bin(exist), n))



if __name__ == '__main__':

    obj = Solution()
    A = [1,1]
    print('input: {}'.format(A))
    r = obj.findErrorNums(A)
    print('output: {}'.format(r))