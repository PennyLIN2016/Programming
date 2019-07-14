import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        #Runtime: 32 ms, faster than 96.52% of Python online submissions for Find K Pairs with Smallest Sums.
        #Memory Usage: 12.1 MB, less than 66.82% of Python online submissions for Find K Pairs with Smallest Sums.
        #time: heapq  o(nlgn) space :0(k)
        if not nums1 or not nums2 or k<=0: return []
        res=[]
        heapList=[]
        for i in range(min(len(nums1),k)):
            heapq.heappush(heapList,(nums1[i]+nums2[0],i,0))
        while len(res)<min(k,len(nums1)*len(nums2)):
            sum_cur,p1,p2= heapq.heappop(heapList)
            res.append([nums1[p1],nums2[p2]])
            if p2+1<len(nums2):
                heapq.heappush(heapList,(nums1[p1]+nums2[p2+1],p1,p2+1))
        return res

if __name__ == '__main__':
    object = Solution()
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 2


    r = object.kSmallestPairs(nums1,nums2,k)
    print(r)
    print('---End---')
