class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        # Runtime: 108 ms, faster than 34.78% of Python online submissions for Shopping Offers.
        # Memory Usage: 11.7 MB, less than 60.00% of Python online submissions for Shopping Offers.
        # google solution: dfs solution

        l=len(price)
        res= sum([i*j for i ,j in zip(price,needs)])
        for specialOffice in special:
            if all(specialOffice[i]<=needs[i] for i in range(l)):
                left=[needs[i]-specialOffice[i] for i in range(l)]
                if min(left) >= 0:
                    res=min(res, specialOffice[-1] + self.shoppingOffers(price,special,left))
        return res







if __name__ == '__main__':
    object = Solution()
    #n1=["0:start:0","1:start:2","1:end:5","0:end:6"]
    #n2= 2
    n1= [2,5]
    n2= [[3,0,5],[1,2,10]]
    n3=[3,2]

    print('---Start---')
    print (n1)
    r = object.shoppingOffers(n1,n2,n3)
    print(r)
    print('---End---')