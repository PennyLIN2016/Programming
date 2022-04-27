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


    def findRadius1(self, houses: list[int], heaters: list[int]) -> int:
        # 29 / 30 test cases passed. failed at the case:
        # heaters = houses len(heaters) = 15226 [1..15225, 1522]
        # except: 0 reslut : 13703
        # the failure starts at
        # house-1523 v: 1523 heaterIndex-1521 v-1522 res-1
        # the last one: house-15225 v: 15225 heaterIndex-1521 v-1522 res-13703
        # the reason: When there are repeated value in heaters,the heater index will stop at the repeated value.
        houses.sort()
        heaters.sort()
        res = float('-inf')
        heaterIndex = 0
        i = 0
        for v in houses:
            if v < heaters[heaterIndex]:
                if heaterIndex == 0:
                    d = heaters[heaterIndex] - v
                else:
                    if heaters[heaterIndex] - v <= v - heaters[heaterIndex - 1]:
                        d = heaters[heaterIndex] - v
                    else:
                        d = v - heaters[heaterIndex-1]
            else:
                if heaterIndex == len(heaters) - 1:
                    d = v - heaters[heaterIndex]
                else:
                    while heaterIndex + 1 < len(heaters) and \
                            abs(v - heaters[heaterIndex]) > abs(v - heaters[heaterIndex + 1]):
                        # When there are repeated value in heaters,the heater index will stop at the repeated value.
                        heaterIndex += 1
                    d = abs(v - heaters[heaterIndex])
            res = max(d, res)
            print('house-{} v: {} heaterIndex-{} v-{} res-{}'.format(i, v, heaterIndex, heaters[heaterIndex], res))

            i += 1

        return res

    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        # Runtime: 290 ms, faster than 90.29% of Python3 online submissions for Heaters.
        # Memory Usage: 17.8 MB, less than 26.99% of Python3 online submissions for Heaters.
        # corrected solution of findRadius1. time: o(nlgn) space: o(1)
        houses.sort()
        heaters.sort()
        res = float('-inf')
        heaterIndex = 0
        for v in houses:
            if v < heaters[heaterIndex]:
                if heaterIndex == 0:
                    d = heaters[heaterIndex] - v
                else:
                    if heaters[heaterIndex] - v <= v - heaters[heaterIndex - 1]:
                        d = heaters[heaterIndex] - v
                    else:
                        d = v - heaters[heaterIndex-1]
            else:
                while heaterIndex + 1 < len(heaters) and \
                            abs(v - heaters[heaterIndex]) >= abs(v - heaters[heaterIndex + 1]):
                    heaterIndex += 1
                d = abs(v - heaters[heaterIndex])
            res = max(d, res)

        return res

if __name__ == '__main__':
    object = Solution()
    A= [1,2,3]
    B= [2]
    print('---Start---')
    r = object.findRadius(A,B)
    print(r)
    print('---End---')
