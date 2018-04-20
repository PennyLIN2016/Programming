class Solution(object):
    # my solution 35s
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if not version1 or not version2:
            return 0
        s1 = version1.split('.')
        s2 = version2.split('.')
        for i in range(min(len(s1),len(s2))):
            if int(s1[i])>int(s2[i]):
                return 1
            if int(s1[i])< int(s2[i]):
                return -1

        if len(s1)>len(s2):
            for j in range(len(s2),len(s1)):
                if int(s1[j]) != 0:
                    return 1
            return 0
        if len(s1)<len(s2):
            for j in range(len(s1),len(s2)):
                if int(s2[j]) != 0:
                    return -1
        '''
        a good solution of the rest part but make sure the int() will not too great to float out .
        if (i+1) < len(version1) and int("".join(version1[i+1:])) != 0:
            return 1
        if (i+1) < len(version2) and int("".join(version2[i+1:])) != 0:
            return -1
        '''

        return 0

if __name__ == '__main__':
    v1 = '0.1'
    v2 = '0.1.000.1'

    k = Solution()

    print (k.compareVersion(v1,v2))