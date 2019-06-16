class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        #Runtime: 348 ms, faster than 72.14% of Python online submissions for Maximum Product of Word Lengths.
        #Memory Usage: 12.4 MB, less than 98.31% of Python online submissions for Maximum Product of Word Lengths.
        # time : o(nlgn) space(n)
        if not words: return 0

        letterValue=[0]*len(words)
        for i,value in enumerate(words):
            for char in value:
                # the letterValue is 26 bit: 0b10000000000000000000000011, each bit stands for if a letter
                # duplicate letter just gets 1 in some pos bit.
                letterValue[i]|=1<<(ord(char)-ord('a'))
        res= 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if  not letterValue[i]&letterValue[j]:
                    res= max(res,len(words[i])*len(words[j]))
        return res





if __name__ == '__main__':
    k = Solution()
    s =   ["abcw","baz","foo","bar","xtfn","abcdef"]
    #j = 12
    print s
    r = k.maxProduct(s)

    print(r)
    print('---End---')



