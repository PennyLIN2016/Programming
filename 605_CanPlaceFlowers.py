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