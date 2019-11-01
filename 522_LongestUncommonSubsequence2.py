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




if __name__ == '__main__':
    object = Solution()
    A= ["aba", "cdc", "eae",'1','degfg']



    print('---Start---')
    print A
    r = object.findLUSlength(A)
    print(r)
    print('---End---')
