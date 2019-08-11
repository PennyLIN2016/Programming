import collections
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Runtime: 356 ms, faster than 8.74% of Python online submissions for Reconstruct Original Digits from English.
        #Memory Usage: 12.4 MB, less than 50.00% of Python online submissions for Reconstruct Original Digits from English.
        # other`s solution: to be analyzed
        s_counter= collections.Counter(s)
        nums = ['six', 'zero', 'two', 'eight', 'seven', 'four', 'five', 'nine', 'one', 'three']
        numc = [collections.Counter(num) for num in nums]
        digits = [6, 0, 2, 8, 7, 4, 5, 9, 1, 3]
        res=[0]*10
        for i,value in enumerate(nums):
            n_counter=numc[i]
            t=min(s_counter[c]/n_counter[c] for c in n_counter)
            res[digits[i]]=t
            for j in range(t):
                s_counter.subtract(n_counter)
        return ''.join(str(i)*n for i,n in enumerate(res))

if __name__ == '__main__':
    object = Solution()
    num = "owoztneoer"

    print(num)
    print('---Start---')
    r = object.originalDigits(num)
    print(r)
    print('---End---')
