import collections
class Solution(object):
    #Runtime: 20 ms, faster than 77.36% of Python online submissions for Longest Uncommon Subsequence II.
    #Memory Usage: 11.8 MB, less than 66.67% of Python online submissions for Longest Uncommon Subsequence II.
    def findLUSlength(self, strs):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        def uncommon(s1,s2):
            l1,l2 = len(s1),len(s2)
            p1=p2=0
            while p1<l1 and p2<l2:
                if s1[p1]==s2[p2]:
                    p2+=1
                p1+=1
            return p2!=l2


        if not strs:return -1
        strCount= collections.Counter(strs)
        newStr= sorted(strs,key=len,reverse=True)
        print newStr
        for i,value in enumerate(newStr):
            if strCount[value]>1:continue
            if all(uncommon(p,value) for p in newStr[:i]):
                return len(value)
        return -1

    # Runtime: 51 ms, faster than 56.57% of Python3 online submissions for Longest Uncommon Subsequence II.
    # Memory Usage: 13.9 MB, less than 77.71% of Python3 online submissions for Longest Uncommon Subsequence II.
    # force solution: time: o(m*n**2) space: o(1)
    def findLUSlength(self, strs: list[str]) -> int:
        # s1 is sub of s2
        def isSub(s1, s2):
            pos = 0
            for char in s2:
                if char == s1[pos:pos+1]:
                    pos += 1
            return pos == len(s1)
        strs.sort(key=len, reverse=True)
        for i in range(len(strs)):
            # not a sub string of others
            flag = True
            for j in range(len(strs)):
                if i == j:
                    continue
                if isSub(strs[i], strs[j]):
                    flag = False
                    break
            if flag:
                return len(strs[i])
        return -1


if __name__ == '__main__':
    object = Solution()
    A= ["aba", "cdc", "eae",'1','degfg']



    print('---Start---')
    print A
    r = object.findLUSlength(A)
    print(r)
    print('---End---')
