class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        #Runtime: 12 ms, faster than 93.17% of Python online submissions for Detect Capital.
        #Memory Usage: 11.8 MB, less than 33.33% of Python online submissions for Detect Capital.
        if not word or len(word)==1: return True
        tmp=word
        if word[0].islower() :
            if tmp==word.lower():return True
            else:
                return False
        else:
            if tmp[1:]==tmp[1:].lower() or tmp[1:]==tmp[1:].upper():
                return True
            else:
                return False



if __name__ == '__main__':
    object = Solution()
    A= 'Dgogle'


    print('---Start---')
    print A
    r = object.detectCapitalUse(A)
    #12701
    print(r)
    print('---End---')
