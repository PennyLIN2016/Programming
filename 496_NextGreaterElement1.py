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
if __name__ == '__main__':
    object = Solution()
    A=  [4,1,2]
    B= [1,2,3,4]


    print('---Start---')
    r = object.nextGreaterElement(A,B)
    print(r)
    print('---End---')
