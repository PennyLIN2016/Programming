import heapq
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        #Runtime: 84 ms, faster than 31.23% of Python online submissions for Relative Ranks.
        #Memory Usage: 13.1 MB, less than 33.33% of Python online submissions for Relative Ranks.
        if not nums: return []
        ## guarantee temQ changing will not affect nums
        temQ = nums+[]
        heapq.heapify(temQ)

        rank={}
        rank_n= len(nums)
        while rank_n>0:
            # get and remove the smallest item
            rank[heapq.heappop(temQ)]=rank_n
            rank_n-=1

        res=[]
        for value in nums:
            if rank[value]==1:
                res.append("Gold Medal")
            elif rank[value]==2:
                res.append("Silver Medal")
            elif rank[value]==3:
                res.append("Bronze Medal")
            else:
                res.append(str(rank[value]))
        return res

if __name__ == '__main__':
    object = Solution()
    A= [5, 4, 3, 2, 1]
    print('---Start---')
    print A
    r = object.findRelativeRanks(A)
    print(r)
    print('---End---')
