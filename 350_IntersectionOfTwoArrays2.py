import collections
class Solution(object):
    def intersect1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #Runtime: 56 ms, faster than 33.66% of Python online submissions for Intersection of Two Arrays II.
        #Memory Usage: 11.9 MB, less than 51.50% of Python online submissions for Intersection of Two Arrays II.

        c1= collections.Counter(nums1)
        c2= collections.Counter(nums2)
        fre= []
        for key in c1:
            if key in c2.keys():
                fre.append([key,min(c1[key],c2[key])])
        print fre
        res=[]
        while len(fre)>0:
            tmp = fre.pop()
            res+=[tmp[0] for _ in range(tmp[1])]
        return res
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #Runtime: 56 ms, faster than 33.66% of Python online submissions for Intersection of Two Arrays II.
        #Memory Usage: 11.9 MB, less than 51.50% of Python online submissions for Intersection of Two Arrays II.
        #Runtime: 36 ms, faster than 78.97% of Python online submissions for Intersection of Two Arrays II.
        #Memory Usage: 12 MB, less than 17.65% of Python online submissions for Intersection of Two Arrays II.
        c1= collections.Counter(nums1)
        c2= collections.Counter(nums2)
        # counter.elements()
        return list((c1&c2).elements())

if __name__ == '__main__':
    k = Solution()
    n1 = [4,9,5,4]
    n2 = [9,4,9,8,4]

    r = k.intersect(n1,n2)
    print(r)
    print('---End---')



