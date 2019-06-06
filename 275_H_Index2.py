class Solution(object):
    def hIndex2(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # Runtime: 120 ms, faster than 73.01% of Python online submissions for H-Index II.
        # Memory Usage: 16.4 MB, less than 85.07% of Python online submissions for H-Index II.
        # time: O(logN)，space:O(N)
        if not citations: return 0
        #time  O(NlogN + logN)
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
    print(p.hIndex2(s))