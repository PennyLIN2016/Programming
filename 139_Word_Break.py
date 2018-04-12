class Solution(object):
    def wordBreak(self,s,wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """

        flag = [0]*len(str(s))

        for i in range(len(s)):
            tmp = s[i:]
            if tmp in wordDict:
                flag[i]= 1

        for j in reversed(range(len(s))):
            if not flag[j]:
                for k in range(j+1,len(s)):
                    tmp1 = s[j:k]
                    if tmp1 in wordDict and flag[k]:
                        flag[j] = 1
                        break

        return flag[0]

if __name__ == '__main__':
    dict = ['lee', 'tcode']
    s = 'leetcode'

    k = Solution()

    print ('Ok') if k.wordBreak(s,dict) else print ('Failed')