class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        #Runtime: 72 ms, faster than 81.03% of Python online submissions for Unique Substrings in Wraparound String.
        #Memory Usage: 12.2 MB, less than 100.00% of Python online submissions for Unique Substrings in Wraparound String.
        # time:o(n) space:o(26)=o(1)
        import collections
        counted=collections.defaultdict(int)
        l=0
        for i in range(len(p)):
            if i>0 and (ord(p[i])==ord(p[i-1])+1 or (p[i]=='a'and p[i-1]=='z')):
                l+=1
            else:
                l=1
            counted[p[i]]=max(l,counted[p[i]])
        return sum(counted.values())
import collections


class Solution:
    def findSubstringInWraproundString1(self, p: str) -> int:
        # brutal solution : time out
        # time: o(n**2) space: o(n)
        l = len(p)
        res = 0
        dp = set()
        for i in range(l):
            for cur in range(1, l-i+1):
                tmp = p[i:i+cur]
                if tmp in dp:
                    continue
                dp.add(tmp)
                if cur == 1:
                    res += 1
                else:
                    if (p[i+cur-2] == 'z' and p[i+cur-1] == 'a') \
                            or (ord(p[i + cur - 1]) - ord(p[i + cur - 2]) == 1):
                        res += 1
                    else:
                        break

        return res

    def findSubstringInWraproundString2(self, p: str) -> int:
        # Runtime: 98 ms, faster than 78.70% of Python3 online submissions for Unique Substrings in Wraparound String.
        # Memory Usage: 14.1 MB, less than 42.01% of Python3 online submissions for Unique Substrings in Wraparound String.
        # add 'z' in front of 'a' to ensure the pattern includes all possible acceptable substring
        pattern = 'zabcdefghijklmnopqrstuvwxyz'
        # store the max substring length, which ends with some char
        cMax = collections.defaultdict(int)
        cur = 0
        for i in range(len(p)):
            # skip i = 0
            # p[i-1:i+1] in pattern:the i char is the correct one
            if i and p[i-1:i+1] not in pattern:
                # clear up
                cur = 1
            else:
                # i == 0
                # or accepted substring is extended by 1
                cur += 1
            cMax[p[i]] = max(cur, cMax[p[i]])

        return sum(cMax.values())

    def findSubstringInWraproundString(self, p: str) -> int:
        # Runtime: 118 ms, faster than 59.76% of Python3 online submissions for Unique Substrings in Wraparound String.
        # Memory Usage: 14.1 MB, less than 42.01% of Python3 online submissions for Unique Substrings in Wraparound String.
        # store the max substring length, which ends with some char
        # to avoid count the same substring repeatedly
        cMax = collections.defaultdict(int)
        # current counting substring length
        # if there is an accepted substring with l length, there would be l acceptable substrings.
        cur = 0
        for i in range(len(p)):
            if i and ((p[i] == 'a' and p[i-1] == 'z') or (ord(p[i]) - ord(p[i-1]) == 1)):
                #accepted substring is extended by 1
                cur += 1
            else:
                cur = 1
            cMax[p[i]] = max(cur, cMax[p[i]])

        return sum(cMax.values())

if __name__ == '__main__':
    object = Solution()
    A=  'zab'
    print('---Start---')
    r = object.findSubstringInWraproundString(A)
    print(r)
    print('---End---')
