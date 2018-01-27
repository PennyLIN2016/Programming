
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return None

        set_in = {}
        for i in xrange(len(strs)):
            tmp =[]
            for j in xrange(len(strs[i])):
                tmp.append(strs[i][j])
            tmp.sort()
            key_s = ''.join(tmp)
            if not  set_in.has_key(key_s):
                str_l = []
                str_l.append(strs[i])
                set_in[key_s]=str_l
            else:
                str_l = set_in[key_s]
                str_l.append(strs[i])
                set_in.update({key_s:str_l})

        return  set_in.values()

if __name__ == '__main__':

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    k = Solution()
    print 'input :',strs
    r = k.groupAnagrams(strs)
    print  'result : ',r


