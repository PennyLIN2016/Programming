import collections
class Solution(object):
    def distributeCandies1(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # Runtime: 912 ms, faster than 11.00% of Python online submissions for Distribute Candies.
        # Memory Usage: 13.6 MB, less than 33.33% of Python online submissions for Distribute Candies.
        # my own solution: time o(n) space o(n)
        if not candies: return 0
        count= collections.Counter(candies)
        return min(int(len(candies)/2) ,len(count))

    def distributeCandies2(self, candies):
        # Runtime: 836 ms, faster than 24.32% of Python online submissions for Distribute Candies.
        # Memory Usage: 13.4 MB, less than 83.33% of Python online submissions for Distribute Candies.
        # my own soltuion2 : time : o(n) space:o(n)
        if not candies:return 0
        types=set()
        l,count=len(candies),0
        for index in range(l):
            if candies[index] not in types:
                count+=1
        return min(int(l/2) ,count)

    def distributeCandies(self, candies):
        # Runtime: 772 ms, faster than 58.34% of Python online submissions for Distribute Candies.
        # Memory Usage: 13.5 MB, less than 66.67% of Python online submissions for Distribute Candies.
        # google solution: set(list[]) //2 integer division time :o(n) space: o(n)
        return min(len(set(candies)),len(candies)//2)
   # python 3 soltion 

        # Runtime: 884 ms, faster than 76.76% of Python3 online submissions for Distribute Candies.
        # Memory Usage: 16.3 MB, less than 37.42% of Python3 online submissions for Distribute Candies.
        # time: o(n) space: o(1)
        types = set(candyType)
        return min(len(candyType)//2, len(types))


if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1 = [1,1,2,2,3,3]


    print('---Start---')
    print (n1)
    r = object.distributeCandies(n1)
    print(r)
    print('---End---')
