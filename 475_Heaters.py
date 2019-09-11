class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        #Runtime: 224 ms, faster than 100.00% of Python online submissions for Heaters.
        #Memory Usage: 14.6 MB, less than 33.33% of Python online submissions for Heaters.
        #time: o(nlgn) time(1)
        houses.sort()
        heaters.sort()
        res,pos=0,0
        heaters=[float('-inf')]+heaters+[float('inf')]
        for v in houses:
            # the current house between two heaters
            while v>=heaters[pos]:
                pos+=1
            # get the smaller r to the two closest heaters
            r=min(v-heaters[pos-1],heaters[pos]-v)
            res=max(res,r)
        return res







if __name__ == '__main__':
    object = Solution()
    A= [1,2,3]
    B= [2]
    print('---Start---')
    r = object.findRadius(A,B)
    print(r)
    print('---End---')
