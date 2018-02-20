class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1= m-1
        p2 = n-1
        p3 = n+m-1

        while p1 >= 0 and p2>= 0 and p3>=0:
            if nums1[p1]>= nums2[p2]:
                nums1[p3]= nums1[p1]
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1

        while  p2>= 0:
            nums1[p3] = nums2[p2]
            p3-=1
            p2-=1

        return



if __name__ == '__main__':
    list1 = [1,2,4,7,9,0,0,0,0]
    list2 = [5,7,8,12]

    k = Solution()
    k.merge(list1,5,list2,4)

    print 'the Result :',list1




