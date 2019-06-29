class Solution(object):
    def intersection1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #Runtime: 28 ms, faster than 94.49% of Python online submissions for Intersection of Two Arrays.
        #Memory Usage: 12 MB, less than 21.27% of Python online submissions forIntersection of Two Arrays.
        # time: o(n), space : o(n)
        set1= set(nums1)
        set2= set(nums2)
        res=[]
        for value in set1:
            if value in set2:
                res.append(value)
        return res
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #Runtime: 20 ms, faster than 99.87% of Python online submissions for Intersection of Two Arrays.
        #Memory Usage: 12 MB, less than 17.45% of Python online submissions for Intersection of Two Arrays.
        # time: o(n), space : o(n)
        set1= set(nums1)
        set2= set(nums2)
        return list(set1.intersection(set2))

if __name__ == '__main__':
    k = Solution()
    n1 = [4,9,5]
    n2 = [9,4,9,8,4]

    r = k.intersection(n1,n2)
    print(r)
    print('---End---')



