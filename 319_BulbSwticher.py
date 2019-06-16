class Solution(object):
    def bulbSwitch1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # time out: brutal solution
        # time: O(n*2) space : O(n)
        if n<=0: return 0
        if n <= 2: return 1
        bulbs= []
        for i in range(int(n/2)):
            bulbs+=[1,0]
        if n%2==1:
            bulbs+=[1]
        #print(bulbs)
        k = 3
        while k-1<n:
            for i in range(int(n/k)):
                if bulbs[k*(i+1)-1]==1:
                   bulbs[k*(i+1)-1]=0
                else:
                    bulbs[k*(i+1)-1]=1
            #print(bulbs)
            k+=1
        return sum(bulbs)
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Runtime: 16 ms, faster than 89.88% of Python online submissions for Bulb Switcher.
        #Memory Usage: 11.8 MB, less than 33.96% of Python online submissions for Bulb Switcher.
        # matchematic solution:  for i , if the quantity number fo toggling is odd, the bulb should be on.
        # for i, for example 8, can be toggled in 1,2,4,8 loop. so the bulb should be off. so the quantity nubmer of factors is the times.
        # mathematically, if only square number can have odd quantity of factors. other factors should be a pair : for example,6 [1,6][2,3]
        # so the solution is to find how many square numbers within [1,n]
        # time : o(1) spaceo(1)
        import math
        if n<=0 :return 0
        return int(math.sqrt(n))
        # or return (int(n**0.5))

if __name__ == '__main__':
    k = Solution()

    j = 78

    r = k.bulbSwitch(j)

    print(r)
    print('---End---')



