class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows<= 0:
            return []
        if numRows == 1:
            return [[1]]
        r = [[1]]
        for i in xrange(1,numRows):
            #tmp = [1 for i in xrange(i+1)]
            tmp = [1]* (i+1)
            pre = r[-1]
            for j in xrange(1,i):
                tmp[j]= pre[j-1]+pre[j]
            r.append(tmp)
        return r

if __name__ == '__main__':


    inputs = 9

    k = Solution()
    r = k.generate(inputs)

    print r
