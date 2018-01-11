
class question(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        tmp_pre = strs[0]
        for i in range (1,len(strs)):
            while strs[i].find(tmp_pre)!= 0:
                if len(tmp_pre)>1:
                        tmp_pre = tmp_pre[:-1]
                else:
                    return ''
        return tmp_pre


if __name__ == '__main__':

    inputs = ['','','','']
    k = question()
    print 'Input :', inputs
    r = k.longestCommonPrefix(inputs)
    print  'Result : ',r



