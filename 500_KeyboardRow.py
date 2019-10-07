class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        #Runtime: 16 ms, faster than 70.11% of Python online submissions for Keyboard Row.
        #Memory Usage: 11.6 MB, less than 85.71% of Python online submissions for Keyboard Row.
        if not words: return []
        l1=('q','w','e','r','t','y','u','i','o','p')
        l2=('a','s','d','f','g','h','j','k','l')
        l3=('z','x','c','v','b','n','m')
        res=[]
        for value in words:
            if not value: continue
            cur= value.lower()
            if cur[0] in l1: l=l1
            elif cur[0] in l2: l=l2
            elif cur[0] in l3: l=l3
            else:
                continue
            res.append(value)
            for i in range(1,len(cur)):
                if cur[i] not in l:
                    res.pop()
                    break
        return res


if __name__ == '__main__':
    object = Solution()
    A=  ["Hello", "Alaska", "Dad", "Peace"]


    print('---Start---')
    r = object.findWords(A)
    print(r)
    print('---End---')
