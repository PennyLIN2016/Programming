class Solution(object):
    def findRestaurant1(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # Runtime: 208 ms, faster than 26.37% of Python3 online submissions for Minimum Index Sum of Two Lists.
        # Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Minimum Index Sum of Two Lists.
        # my own solution; time:o((l1+l2)*n) space:o(l1+l2)
        s= set(list1)&set(list2)
        res={}
        minC= float('inf')
        for value in s:
            cursum=list1.index(value)+list2.index(value)
            if cursum in res:
                res[cursum].append(value)
            else:
                res[cursum]=[value]
            minC = min(cursum, minC)

        return res[minC]
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # Runtime: 116 ms, faster than 83.11% of Python online submissions for Minimum Index Sum of Two Lists.
        # Memory Usage: 12.4 MB, less than 25.00% of Python online submissions for Minimum Index Sum of Two Lists.
        # google solution : time:o(n) space: o(n)
        d1 = {word:ind for ind, word in enumerate(list1)}
        d2 = {word: ind for ind, word in enumerate(list2)}
        res=[]
        # a real nums is faster than float('inf')
        small= 10000
        for word in d1:
            if word in d2:
                curs=d1[word]+d2[word]
                if small>curs:
                    small=curs
                    res=[word]
                elif small==curs:
                    # res only store the cur small sum array
                    res.append(word)
        return res
    
    ##############python3
        def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        # Runtime: 158 ms, faster than 93.32% of Python3 online submissions for Minimum Index Sum of Two Lists.
        # Memory Usage: 14.3 MB, less than 98.90% of Python3 online submissions for Minimum Index Sum of Two Lists.
        # time: o(n) space: o(n)
        dictList1 = {}
        for i, v in enumerate(list1):
            dictList1[v] = i
        cur = float('inf')
        res = []
        for j, value in enumerate(list2):
            if value in dictList1:
                if j + dictList1[value] < cur:
                    cur = j + dictList1[value]
                    res = [value]
                elif j + dictList1[value] == cur:
                    res.append(value)
        return res
    

if __name__ == '__main__':
    object = Solution()
    #n1= [[1,1,0],[1,1,0],[0,0,1]]
    n1= ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    n2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]


    print('---Start---')
    print (n1)
    r = object.findRestaurant(n1,n2)
    print(r)
    print('---End---')
