class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # Runtime: 24 ms, faster than 72.32% of Python online submissions for H-Index.
        # Memory Usage: 12 MB, less than 22.62% of Python online submissions for H-Index.
        # time: O(NlogN + logN)，space:O(N)
        if not citations: return 0
        #time  O(NlogN + logN)
        citations.sort()
        r,l,h= len(citations)-1,0,0
        while r>=l:
            # bs
            pos = int((l+r)/2)
            # min(citations[pos],len(citations)-pos) matches the definition of h
            h = max(h,min(citations[pos],len(citations)-pos))
            if citations[pos]<len(citations)-pos:
                l = pos+1
            else:
                r = pos-1
        return h

if __name__ == '__main__':
    s= [3,0,6,1,5,0,9,8,7]

    p = Solution()
    print(p.hIndex(s))