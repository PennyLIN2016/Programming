class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Runtime: 124 ms, faster than 63.90% of Python online submissions for First Unique Character in a String.
        #Memory Usage: 13 MB, less than 21.66% of Python online submissions for First Unique Character in a String.
        # time :o(n) space:o(n)
        if not s: return -1
        first= {}
        for i in range(len(s)):
            if s[i] not in first:
                first[s[i]]=i
            else:
                first[s[i]]= len(s)+1
        pos= len(s)+1
        for v in list(first):
            pos= min(pos,first[v])
        return pos if pos!=len(s)+1 else -1
    
     def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Runtime: 231 ms, faster than 40.11% of Python online submissions for First Unique Character in a String.
        #Memory Usage: 13.5 MB, less than 96.04% of Python online submissions for First Unique Character in a String.
        # time: o(n) space: o(n)
        import collections
        countDict = collections.Counter(s)
        for i, v in enumerate(s):
            if countDict[v] == 1:
                return i
     def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """
        firstPos = {}
        for i, v in enumerate(s):
            if v in firstPos:
                firstPos[v] = float('inf')
            else:
                firstPos[v] = i

        res = min(firstPos.values())

        return -1 if res == float('inf') else res

        return -1


if __name__ == '__main__':
    object = Solution()
    k = "loveleetcode"

    r = object.firstUniqChar(k)
    print(r)
    print('---End---')
