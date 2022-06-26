class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # Runtime: 70 ms, faster than 32.72% of Python online submissions for Top K Frequent Words.
        # Memory Usage: 13.5 MB, less than 90.81% of Python online submissions for Top K Frequent Words.
        # heapq solution: heapq can easily implement sorted by multi parameters.
        # time: oo(nlgk) space: o(n)
        import collections
        import heapq
        cnt = collections.Counter(words)
        hq = []
        # time: o(lgn)
        for key, v in cnt.items():
            heapq.heappush(hq, [-v, key])
        return [heapq.heappop(hq)[1] for _ in range(k)]


obj = Solution()
t1 = ["i","love","leetcode","i","love","coding"]

t2 = 2
print(obj.topKFrequent(t1, t2))
