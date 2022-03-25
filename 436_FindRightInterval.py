class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        #Runtime: 300 ms, faster than 42.79% of Python online submissions for Find Right Interval.
        #Memory Usage: 18.1 MB, less than 50.00% of Python online submissions for Find Right Interval.
        def bigger_find(start,v):
            l,r=0,len(start)-1
            first=-1
            while l<=r:
                mid=(l+r)//2
                if start[mid]>=v:
                    r=mid-1
                    first=mid
                else:
                    l=mid+1
            return first
        n=len(intervals)
        start_m={v[0]:i for i,v in enumerate(intervals)}
        start_l=[v[0] for v in intervals]
        res=[]
        start_l.sort()
        for v in intervals:
            pos=bigger_find(start_l,v[1])
            res.append(start_m[start_l[pos]] if pos!=-1 else -1)
        return res


    
   def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # brutal solution: timeout
        m = len(intervals)
        if m == 1:
            return [-1]
        #print('res-{}'.format(res))
        tmp = []
        for i, v in enumerate(intervals):
            tmp.append([v[0], v[1], i])
        tmp.sort()
        print('tmp-{}'.format(tmp))
        res = [-1] * m
        for i, v in enumerate(intervals):
            for j, value in enumerate(tmp):
                if v[0] == value[0]:
                    continue
                if v[1] <= value[0]:
                    res[i] = value[2]
                    break
        return res
    
   def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # Runtime: 230 ms, faster than 100.00% of Python online submissions for Find Right Interval.
        # Memory Usage: 18.9 MB, less than 87.27% of Python online submissions for Find Right Interval.
        # bisect solution time: o(n*nlgn) time: o(n)
        m = len(intervals)
        if m == 1:
            return [-1]
        # o(nlgn)
        tmp = sorted((v[0], i, v[1]) for i, v in enumerate(intervals))
        #print(tmp)
        res = [-1] * m
        for v in tmp:
            # o(nlgn)
            r = bisect.bisect_left(tmp, (v[2],))
            if r < m:
                res[v[1]] = tmp[r][1]
        return res







if __name__ == '__main__':
    object = Solution()
    num =  [ [3,4], [2,3], [1,2] ]

    print(num)
    print('---Start---')
    r = object.findRightInterval(num)
    print(r)
    print('---End---')
