class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex< 0:
            return []
        if rowIndex == 0:
            return [1]
        pre  = [1]
        for i in xrange(1,rowIndex+1):
            tmp = [1]* (i+1)
            for j in xrange(1,i):
                tmp[j]= pre[j-1]+pre[j]
            pre = tmp
        return pre

if __name__ == '__main__':


    inputs = 4

    k = Solution()
    r = k.getRow(inputs)

    print r
