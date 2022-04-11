import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Runtime: 60 ms, faster than 47.68% of Python online submissions for Sort Characters By Frequency.
        #Memory Usage: 14.8 MB, less than 33.33% of Python online submissions for Sort Characters By Frequency.
        # time: o(nlgn) space:o(n)
        if not s: return s
        countdict=dict(collections.Counter(s))
        dict_fre= {}
        for v in countdict:
            tmp=[v]*countdict[v]
            if countdict[v] not in dict_fre:
                dict_fre[countdict[v]]=''.join(tmp)
            else:
                dict_fre[countdict[v]]+=''.join(tmp)
        order=sorted(dict_fre.keys(),reverse=True)
        res=''
        for f in order:
            res+=dict_fre[f]
        return res
    
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Runtime: 52 ms, faster than 79.03% of Python online submissions for Sort Characters By Frequency.
        #Memory Usage: 15.9 MB, less than 65.86% of Python online submissions for Sort Characters By Frequency.
        # space: o(n)
        import collections
        # time : o(n)
        cnt = collections.Counter(s)
        # time : o(nlogk): k = len(cnt) ==> o(nlogn)
        # 
        freCnt = cnt.most_common(len(cnt))
        res = ''
        for v in freCnt:
            tmp = v[0] * v[1]
            res += tmp
        return res

if __name__ == '__main__':
    object = Solution()
    num =  "tkreek"

    print(num)
    print('---Start---')
    r = object.frequencySort(num)
    print(r)
    print('---End---')
