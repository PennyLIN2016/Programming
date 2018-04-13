import collections
class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        '''
        dic = collections.defaultdict(list)

        def dfs(s):
            if not s:
                return [None]
            if s in dic:
                return dic[s]
            res = []
            for word in wordDict:
                n = len(word)
                if s[:n] == word:
                    for r in dfs(s[n:]):
                        if r:
                            res.append(word + " " + r)
                        else:
                            res.append(word)
            dic[s] = res
            return res

        return dfs(s)
        '''

        def match_s(s,words,res,r_tmp):
            if s =='':
                # make sure the list in the res will not change in line with r_tmp
                res.append(r_tmp[:])

                return

            for i in reversed(range(len(s))):
                tmp_left = s[:i+1]
                if tmp_left in words:
                    tmp_right = s[i+1:]
                    words.remove(tmp_left)
                    r_tmp.append(tmp_left)
                    match_s(tmp_right,words,res,r_tmp)
                    r_tmp.pop()
                    words += [tmp_left]

        res = []
        r_tmp = []
        wordset = wordDict[:]

        match_s(s[:],wordset,res,r_tmp)
        return res


if __name__ == '__main__':
    s = 'catsanddog'
    dic_s = ['cat', 'cats', 'and', 'sand', 'dog']

    k = Solution()
    r = k.wordBreak(s,dic_s)
    print (r)
