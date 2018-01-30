class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        if len(intervals)<=1:
            return intervals

        pos = 0
        tmp_int = sorted(intervals,key = lambda x:x.start)
        for i in xrange(1,len(tmp_int)):
            if tmp_int[i].start <= tmp_int[pos].end:
                tmp_int[pos].end = max(tmp_int[i].end,tmp_int[pos].end)
            else:
                pos += 1
                tmp_int[pos]= tmp_int[i]
        return tmp_int[:pos+1]



if __name__ == '__main__':

    k = Solution()
    A = [[1,3],[2,6],[8,10],[15,18]]
    Interval_input = []
    for i in  xrange(len(A)):
        t = Interval()
        t.start = A[i][0]
        t.end = A[i][1]
        Interval_input.append(t)


    #A = [3,2,1,0,4]
    #A = [2,0]

    r= k.merge(Interval_input)
    print '----Result-----'
    for j in  xrange(len(r)):
        print'[', r[j].start,
        print r[j].end,'],',
    print




