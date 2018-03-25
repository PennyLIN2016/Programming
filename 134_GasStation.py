class Solution(object):
    def canCompleteCircuit1(self, gas, cost):# time limit exceed
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost:
            return -1
        if len(gas)!= len(cost):
            return -1

        if len(gas) == 1:
            if gas[0] < cost[0]:
                return -1
            else:
                return 0

        for i in xrange(len(gas)):
            sum_gas = 0
            for j in xrange(len(gas)):
                pos = (i+j)% len(gas)
                sum_gas = sum_gas + gas[pos]-cost[pos]
                if sum_gas< 0 :
                    break
            if sum_gas >= 0:
                return i
        return -1
    def canCompleteCircuit(self, gas, cost):# passed
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost:
            return -1
        if len(gas) != len(cost):
            return -1

        start = 0
        lack = 0
        left = 0
        for i in xrange(len(gas)):
            left += gas[i]-cost[i]
            if left <0:
                start = i+1
                lack += left
                left = 0

        if left + lack < 0 :
            start = -1
        return start

if __name__ == '__main__':

    g = [4]
    c = [5]

    k = Solution()

    r= k.canCompleteCircuit(g,c)
    print r
