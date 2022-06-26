class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #Runtime: 96 ms, faster than 64.33% of Python online submissions for Top K Frequent Elements.
        #Memory Usage: 18.8 MB, less than 5.04% of Python online submissions for Top K Frequent Elements.
        # bucket sort solution: time : o(n) space o(n)

        # dict save the frequency
        element_dic= {}
        for value in nums:
            element_dic[value]=element_dic[value]+1 if value in element_dic else 1
        # bucket array: the index stands for the frequency
        fre_array = [[] for i in range(len(nums)+1)]
        for val in element_dic:
            fre_array[element_dic[val]].append(val)
        res =[]
        # get the top k frequency .
        for j in range(len(fre_array)-1,-1,-1):
            if fre_array[j]!= []:
                res.extend(fre_array[j])
            if len(res)==k:
                return res

        return res
    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numberDict = dict()
        for v in nums:
            if v in list(numberDict.keys()):
                numberDict[v] += 1
            else:
                numberDict[v] = 1
        freqDict = dict()
        for key, v in numberDict.items():
            if -v in freqDict.keys():
                freqDict[-v].append(key)
            else:
                freqDict[-v] = [key]

        import heapq
        targetF = freqDict.keys()
        heapq.heapify(targetF)
        res = []
        while len(res) < k:
            f = heapq.heappop(targetF)
            res += freqDict[f]
        return res

   def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # counter solution
        # Runtime: 133 ms, faster than 44.71% of Python online submissions for Top K Frequent Elements.
        # Memory Usage: 16.8 MB, less than 59.41% of Python online submissions for Top K Frequent Elements.
        import collections
        cnt = collections.Counter(nums)
        # most_common: time: o(nlgk)
        return [v[0] for v in cnt.most_common(k)]
    
if __name__ == '__main__':
    k = Solution()
    n1 = [1,1,1,2,2,3]
    t= 2

    r = k.topKFrequent(n1,t)
    print(r)
    print('---End---')



