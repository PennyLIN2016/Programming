class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # Runtime: 136 ms, faster than 98.13% of Python online submissions for Can Place Flowers.
        # Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Can Place Flowers.
        # google solution: greedy solution: time: o(n) space:o(1)
        if n==0: return True
        res=0
        for i ,value in enumerate(flowerbed):
            if value:continue
            if i>0 and flowerbed[i-1]:continue
            if i<len(flowerbed)-1 and flowerbed[i+1]:continue
            res+=1
            flowerbed[i]=1
        return res>=n
    
    ######python3 
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Runtime: 281 ms, faster than 24.49% of Python3 online submissions for Can Place Flowers.
        # Memory Usage: 14.3 MB, less than 74.08% of Python3 online submissions for Can Place Flowers.
        # time: o(n) space:o(1)
        tmp = [0] + flowerbed + [0]
        zeroCnt = 0
        for v in tmp:
            if v == 0:
                zeroCnt += 1
            else:
                n -= int((zeroCnt - 1)/2)
                zeroCnt = 0
            if n <= 0:
                return True
        print('zeroCnt: {} n: {}'.format(zeroCnt, n))
        return int((zeroCnt - 1)/2) >= n


if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1= [1,0,0,0,1]
    n2=1


    print('---Start---')
    print (n1)
    r = object.canPlaceFlowers(n1,n2)
    print(r)
    print('---End---')
