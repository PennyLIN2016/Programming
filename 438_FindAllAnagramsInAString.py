import collections
class Solution(object):
    def findAnagrams1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # my solution: timeout
        from collections import Counter
        pExample=Counter(p)
        res=[]
        for i in range(len(s)-len(p)+1):
            tmp=s[i:i+len(p)]
            tmpE=Counter(tmp)
            if tmpE==pExample:
                res.append(i)
        return res

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # my solution: timeout
        #Runtime: 200 ms, faster than 20.85% of Python online submissions for Find All Anagrams in a String.
        #Memory Usage: 12.6 MB, less than 88.24% of Python online submissions for Find All Anagrams in a String.
        # collection.counter(): time o(n)
        from collections import Counter
        answer = []
        m, n = len(s), len(p)
        if m < n:
            return answer
        pCounter = Counter(p)
        sCounter = Counter(s[:n-1])
        for index in xrange(n - 1, m):
            # do not use counter again, which is time consuming.
                sCounter[s[index]] += 1
                if sCounter == pCounter:
                    answer.append(index - n + 1)
                sCounter[s[index - n + 1]] -= 1
                if sCounter[s[index - n + 1]] == 0:
                    del sCounter[s[index - n + 1]]
        return answer
    
    def findAnagrams1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # brutal solution: 33 / 61 test cases passed. timeout
        # time: o(n*n)
        m, n = len(s), len(p)
        if m < n: return []
        target = collections.Counter(p)
        res = []
        for i in range(m-n+1):
            # time : o(n)
            tmp1 = collections.Counter(s[i:i+n])
            if tmp1 == target:
                res.append(i)
        return res

    def findAnagrams(self, s, p):
        # Runtime: 160 ms, faster than 54.46% of Python online submissions for Find All Anagrams in a String.
        # Memory Usage: 14.4 MB, less than 70.78% of Python online submissions for Find All Anagrams in a String.
        # time: o(n) space: o(n)
        m, n = len(s), len(p)
        if m < n: return []
        # o(n)
        target = collections.Counter(p)
        cur = collections.Counter(s[:n])
        print('target: {} first: {}'.format(target, cur))
        i = 0
        res = []
        # o(n)
        while i < m-n+1:
            if cur == target:
                res.append(i)
            if cur[s[i]] == 1:
                del cur[s[i]]
            else:
                cur[s[i]] -= 1
            if i+n < m:
                cur[s[i+n]] += 1
            i += 1
            print('i: {} res: {} first: {}'.format(i, res, cur))
        return res
    
if __name__ == '__main__':
    object = Solution()
    num =  "cbaebabacd"
    p="abc"
    #num="abab"
    #p="ab"

    print(num)
    print('---Start---')
    r = object.findAnagrams(num,p)
    print(r)
    print('---End---')
