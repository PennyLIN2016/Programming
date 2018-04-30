class Solution(object):
    # my solution: time limit exceeded, 31/32 tested cases passed
    def findRepeatedDnaSequences1(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<=10:
            return []
        r = []
        for i in range(0,len(s)-11):
            tmp_s = s[i:i+10]
            if ''.join(tmp_s) in r:
                continue
            left = s[0:i]
            right = s[i+1:]
            if ''.join(tmp_s) in ''.join(left):
                r.append(''.join(tmp_s))
                continue
            if ''.join(tmp_s) in ''.join(right):
                r.append(''.join(tmp_s))
                continue
        return r
    # a good solution 96s
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        map_d = {}
        r = []

        for i in range(len(s)-9):
            tmp_s = s[i:i+10]
            if tmp_s in map_d:
                if map_d[tmp_s] == 1:
                    r.append(tmp_s)
                map_d[tmp_s]+=1
            else:
                map_d[tmp_s] = 1
        return r




if __name__ == '__main__':

    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    #s = 'AAAAAAAAAA'

    k = Solution()

    print (k.findRepeatedDnaSequences(s))