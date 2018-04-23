from functools import cmp_to_key
class Solution:
    # @param {integer[]} nums
    # @return {string}
    # a good solution 49s
    def largestNumber(self, nums):
        if len(nums)== 0:
            return ''
        if sum(nums)== 0:
            return '0'

        tmp_str = ['']*len(nums)
        for i,val in enumerate(nums):
            tmp_str[i] = str(val)
        # in Python: tmp_str.sort(cmp = lambda s1, s2: 1 if s1 + s2 > s2 + s1 else -1, reverse=True) and do not need to import functools
        tmp_str.sort(key=cmp_to_key(lambda s1, s2: 1 if s1 + s2 > s2 + s1 else -1), reverse=True)
        return ''.join(tmp_str)


if __name__ == '__main__':
    a = [3, 30, 32, 5, 9]
    k = Solution()
    print (k.largestNumber(a))