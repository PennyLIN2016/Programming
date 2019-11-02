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






if __name__ == '__main__':
    object = Solution()
    s = "abpcplea"
    d = ["ale","apple","monkey","plea",]




    print('---Start---')
    print s
    r = object.findLongestWord(s,d)
    print(r)
    print('---End---')
