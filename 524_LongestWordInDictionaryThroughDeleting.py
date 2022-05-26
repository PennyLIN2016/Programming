class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        #Runtime: 380 ms, faster than 52.26% of Python online submissions for Longest Word in Dictionary through Deleting.
        #Memory Usage: 16.8 MB, less than 100.00% of Python online submissions for Longest Word in Dictionary through Deleting.
        # time o(nlgn) space: o(1)
        # check if that is a substring
        def isSub(parent,child):
            lp,lc=len(parent),len(child)
            pp,pc=0,0
            while pp<lp and pc<lc:
                if parent[pp]==child[pc]:
                    pc+=1
                pp+=1
            return pc==lc

        if not s: return ""
        # time: o(nlgn)+o(nlgn)
        d.sort()
        tmp=sorted(d,key= len,reverse=True)
        for value in tmp:
            # isSub: o(len(value))
            if isSub(s,value):return value
        return ""


    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        # Runtime: 648 ms, faster than 42.53% of Python3 online submissions for Longest Word in Dictionary through Deleting.
        # Memory Usage: 16.2 MB, less than 99.37% of Python3 online submissions for Longest Word in Dictionary through Deleting.
        # time: O(n*m) space: o(1)
        def findWord(strCur):
            pos = 0
            for char in s:
                if char == strCur[pos]:
                    pos += 1
                if pos == len(strCur):
                    return True
            return False
        res = ''
        for v in dictionary:
            if findWord(v):
                if len(v) > len(res):
                    res = v
                elif len(v) == len(res) and v < res:
                    res = v

        return res



if __name__ == '__main__':
    object = Solution()
    s = "abpcplea"
    d = ["ale","apple","monkey","plea",]




    print('---Start---')
    print s
    r = object.findLongestWord(s,d)
    print(r)
    print('---End---')
