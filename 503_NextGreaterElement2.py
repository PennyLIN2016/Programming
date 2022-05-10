import collections
class Solution(object):
    def nextGreaterElements1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # brutal solution: time out : 217 / 224 test cases passed.
        if not nums: return []
        max_n= max(nums)
        res=[]
        for i ,value in enumerate(nums):
            print("i: "+ str(i) + '  value: '+ str(value))
            print res
            if value == max_n:
                res.append(-1)
                continue
            for j in range(len(nums)):
                pos=(j+i+1)%len(nums)
                if nums[pos]>value:
                    res.append(nums[pos])
                    break
        return res
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Runtime: 208 ms, faster than 64.26% of Python online submissions for Next Greater Element II.
        #Memory Usage: 13.8 MB, less than 25.00% of Python online submissions for Next Greater Element II.
        res=[-1]* len(nums)
        s=[]
        # the loop is executed twice
        for i in range(len(nums))*2:
            while s and (nums[s[-1]]<nums[i]):
                res[s.pop()]=nums[i]
            s.append(i)
        return res
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        # Runtime: 354 ms, faster than 31.21% of Python3 online submissions for Next Greater Element II.
        # Memory Usage: 16.9 MB, less than 5.32% of Python3 online submissions for Next Greater Element II.
        # extend the solution of 496_NextGreaterElement1.py
        # time: o(n) space:o(n)
        res = []
        stack = []
        d = {}
        nums1 = nums + nums[:len(nums)-1]
        print('nums1: {} nums: {}'.format(nums1, nums))
        for i, v in enumerate(nums1):
            print('i: {} v: {}'.format(i, v))
            while len(stack) and nums1[stack[-1]] < v:
                d[stack.pop()] = v
            stack.append(i)
            print('stack: {} d: {}'.format(stack, d))

        # time: o(n)
        for j in range(len(nums)):
            res.append(d.get(j, -1))
        return res


if __name__ == '__main__':
    object = Solution()
    A= [1,2,1]
    print('---Start---')
    r = object.nextGreaterElements(A)
    print(r)
    print('---End---')
