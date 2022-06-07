
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Runtime: 12 ms, faster than 89.43% of Python online submissions for Next Greater Element III.
        #Memory Usage: 11.9 MB, less than 25.00% of Python online submissions for Next Greater Element III.
        # google solution: time :o(l) space: o(l)
        s=list(str(n))
        l= len(s)
        i = l-1
        while i>0 and s[i]<=s[i-1]:
            i-=1
        if i==0: return -1
        self.reverse(s,i,l-1)
        for j in range(i,l):
            if s[j]>s[i-1]:
                self.swap(s,i-1,j)
                break
        res= int(''.join(s))
        return -1 if res>1<<31 else res

    def swap(self,nums,p1,p2):
        nums[p1],nums[p2]=nums[p2],nums[p1]

    def reverse(self,nums,i,j):
        for k in range(i, (i + j) / 2 + 1):
            self.swap(nums, k, i + j - k)
    def nextGreaterElement1(self, n: int) -> int:
        # Runtime: 60 ms, faster than 9.71% of Python3 online submissions for Next Greater Element III.
        # Memory Usage: 13.8 MB, less than 77.31% of Python3 online submissions for Next Greater Element III.
        # time: o(n) space: o(1)
        nums = list(str(n))
        l = len(nums)
        for i in range(l-1, -1, -1):
            if i > 0 and nums[i-1] < nums[i]:
                if i == l-1 or nums[-1] == nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    res = int(''.join(nums))
                    return -1 if res > 0x7FFFFFFF else res
                else:
                    for j in range(l-1, i-1, -1):
                        if nums[j] > nums[i-1]:
                            nums[i - 1], nums[j] = nums[j], nums[i - 1]
                            break
                    res = int(''.join(nums[:i]+nums[i:][::-1]))
                return res if res <= 0x7FFFFFFF else -1
        return -1

    def nextGreaterElement(self, n: int) -> int:
        # 从右到左找到第一个降序的数字, index记为i-1, 然后从右到左找到第一个比这个数字大的数字,
        # index记为j, 交换两个数字的值, 然后将i-1之后的序列倒序排列即可. 当降序的数字不存在时,
        # i==0, 返回-1. 当得到的结果超过32-bit时, 也返回-1.
        # Runtime: 42 ms, faster than 45.18% of Python3 online submissions for Next Greater Element III.
        # Memory Usage: 14 MB, less than 25.16% of Python3 online submissions for Next Greater Element III.
        # time: o(n) space: o(n)
        nums = list(str(n))

        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        # nums[i-1] < nums[i]
        if i == 0: return -1

        j = len(nums) - 1
        while nums[j] <= nums[i-1]:
            j -= 1
        # nums[j] > nums[i-1]
        nums[j], nums[i-1] = nums[i-1], nums[j]
        nums[i:] = nums[i:][::-1]
        res = int(''.join(nums))
        if res > 2**31 -1:
            return -1
        return res


if __name__ == '__main__':
    object = Solution()
    #n1= [1000,100,10,2]
    n1=12443322

    print('---Start---')
    print n1
    r = object.nextGreaterElement(n1)
    print(r)
    print('---End---')
