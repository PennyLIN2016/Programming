import collections
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        #Runtime: 444 ms, faster than 15.96% of Python online submissions for 4Sum II.
        #Memory Usage: 34.4 MB, less than 25.00% of Python online submissions for 4Sum II.
        # time : o(n**2) space:o(n**2)
        # for a in A for b in B is different to for a,b in (A,B)
        ab=collections.Counter( a+b for a in A for b in B)
        res= [ab[-c-d] for c in C for d in D]
        return sum(res)
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        # Runtime: 487 ms, faster than 94.74% of Python online submissions for 4Sum II.
        # Memory Usage: 13.9 MB, less than 31.87% of Python online submissions for 4Sum II.
        # separating solution:
        # time: o(n**2) space: o(n**2)
        import collections
        ct = collections.defaultdict(int)
        for a in nums1:
            for b in nums2:
                ct[a+b] += 1
        res = 0
        for c in nums3:
            for d in nums4:
                if (c+d) * -1 in ct:
                    res += ct[(c+d) * -1]
        return res



    def fourSumCount1(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        # brutal solution: timeout: 20/132
        # time: o(n**4)
        l = len(nums1)
        res = 0
        for i1 in range(l):
            for i2 in range(l):
                for i3 in range(l):
                    for i4 in range(l):
                        if nums1[i1] + nums2[i2] + nums3[i3] + nums4[i4] == 0:
                            res += 1
        return res


if __name__ == '__main__':
    object = Solution()
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]

    #print(num)
    print('---Start---')
    r = object.fourSumCount(A,B,C,D)
    print(r)
    print('---End---')
