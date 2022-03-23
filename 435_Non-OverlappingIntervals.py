class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #Runtime: 64 ms, faster than 16.46% of Python online submissions for Non-overlapping Intervals.
        #Memory Usage: 15.5 MB, less than 20.00% of Python online submissions for Non-overlapping Intervals.
        # time:o(nlgn) spaceo(1)
        if len(intervals)<=1:return 0
        intervals.sort(key = lambda x:(x[0],x[1]))
        pos=0
        res1=0
        for i,v in enumerate(intervals):
            if i==0:continue
            if v[0]==intervals[pos][0]:
                res1+=1
            elif v[0]<intervals[pos][1]:
                res1+=1
            else:
                pos=i
        intervals.sort(key = lambda x:(x[1],x[0]))
        pos=0
        res2=0
        for i,v in enumerate(intervals):
            if i==0:continue
            if v[0]==intervals[pos][0]:
                res2+=1
            elif v[0]<intervals[pos][1]:
                res2+=1
            else:
                pos=i

        return min(res1,res2)
    
        def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #Runtime: 1367 ms, faster than 82.19% of Python online submissions for Non-overlapping Intervals.
        # Memory Usage: 59.7 MB, less than 72.56% of Python online submissions for Non-overlapping Intervals.
        # time: o(nlgn) space: o(1)
        # ordered by [0]
        intervals.sort()
        l = len(intervals)
        if l == 1: return 0
        
        # the last left interval
        pre = intervals[0]
        i, res = 0., 0
        while i < l-1:
            i += 1
            if intervals[i][0] >= pre[1]:
                # no overlapping: just slide forward
                pre = intervals[i]
            else:
                # overlapping: need to remove one element
                res += 1
                # pre is the element with smaller end time
                if intervals[i][1] < pre[1]:
                    pre = intervals[i]

        return res

    def eraseOverlapIntervals1(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #Runtime: 52 ms, faster than 83.95% of Python online submissions for Non-overlapping Intervals.
        #Memory Usage: 15.1 MB, less than 40.00% of Python online submissions for Non-overlapping Intervals.
        # time:o(nlgn)  space:o(n)
        if not intervals: return 0
        intervals.sort(key= lambda x:(x[0]))
        print intervals
        res=0
        end=intervals[0][1]
        for i in range(1,len(intervals)):
            # tmp=1 :overlapping
            tmp=1 if end >intervals[i][0] else 0
            # if overlapped, keep the less end
            # if no overlapping,switch end to new value
            end=min(end,intervals[i][1]) if tmp==1 else intervals[i][1]
            res+=tmp
        return res



if __name__ == '__main__':
    object = Solution()
    num =  [[1,4],[2,3],[3,4],[2,4],[2,3]]

    print(num)
    print('---Start---')
    r = object.eraseOverlapIntervals(num)
    print(r)
    print('---End---')
