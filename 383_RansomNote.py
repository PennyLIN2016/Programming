import collections
class Solution(object):
    def canConstruct1(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #Runtime: 104 ms, faster than 33.03% of Python online submissions for Ransom Note.
        #Memory Usage: 12 MB, less than 76.74% of Python online submissions for Ransom Note.
        # collections solution
        if not ransomNote : return True
        if not magazine : return False
        target = collections.Counter(ransomNote)
        mag = collections.Counter(magazine)
        return True if target&mag== target else False

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #Runtime: 56 ms, faster than 66.97% of Python online submissions for Ransom Note.
        #Memory Usage: 12 MB, less than 68.84% of Python online submissions for Ransom Note.
        # time o(n) space(n)
        if not ransomNote : return True
        if not magazine : return False
        count_char={}
        for value in ransomNote:
            if value in count_char.keys():
                count_char[value]+=1
            else:
                count_char[value]=1
        for v in magazine:
            if v in count_char.keys():
                count_char[v]-=1
                if count_char[v]==0:
                    del count_char[v]
                if not count_char:
                    return True

        return False


if __name__ == '__main__':
    object = Solution()
    k = "abdcdt"
    l="fdfadajjuuftgb"


    r = object.canConstruct(k,l)
    print(r)
    print('---End---')
