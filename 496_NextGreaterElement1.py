class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #Runtime: 60 ms, faster than 33.51% of Python online submissions for Next Greater Element I.
        #Memory Usage: 12 MB, less than 14.29% of Python online submissions for Next Greater Element I.
        pos={}
        for i,value in enumerate(nums2):
            pos[value]=i
        res=[-1 for _ in range(len(nums1))]
        for i in range(len(nums1)):
            start= pos[nums1[i]]+1
            for j in range(start,len(nums2)):
                if nums1[i]<nums2[j]:
                    res[i]=nums2[j]
                    break

        return res
    
        def nextGreaterElement1(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Runtime: 165 ms, faster than 13.23% of Python3 online submissions for Next Greater Element I.
        # Memory Usage: 14.2 MB, less than 58.13% of Python3 online submissions for Next Greater Element I.
        # brutal solution: time: o(n*m) space: o(1)
        res = [-1]* len(nums1)
        for i in range(len(nums1)):
            flag = 0
            for v in nums2:
                print('i: {} v: {}'.format(i, v))
                if flag == 1 and v > nums1[i]:
                    res[i] = v
                    break
                if v == nums1[i]:
                    flag = 1

                print('v: {} nums1[i]: {} res: {}, flag: {}'.format(v, nums1[i], res, flag))
        return res

    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Runtime: 86 ms, faster than 40.53% of Python3 online submissions for Next Greater Element I.
        # Memory Usage: 14.1 MB, less than 58.13% of Python3 online submissions for Next Greater Element I.
        # stack solution:
        res = []
        stack = []
        d = {}
        # time: o(n)
        # because nums1 is a sub list of nums2. find
        for v in nums2:
            # stack: all nums not matched before v
            # if stack[-1] >= v: the less num has been all popped out
            # in nums in stack are greater then v
            # d[num]= the next greater value
            while len(stack) and stack[-1] < v:
                d[stack.pop()] = v
            stack.append(v)
        # time: o(m)
        for value in nums1:
            res.append(d.get(value, -1))
        return res

if __name__ == '__main__':
    object = Solution()
    A=  [4,1,2]
    B= [1,2,3,4]


    print('---Start---')
    r = object.nextGreaterElement(A,B)
    print(r)
    print('---End---')
