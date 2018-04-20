class Solution(object):
    # my solution 30s
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        str_n = ''
        while n > 0 :
            cur_n = n % 26
            if cur_n:
                str_n += chr(ord('A')+ cur_n-1)
                n = int(n/26)
            else:
                str_n = str_n + 'Z'
                n = int(n/26)-1
        return str_n[::-1]


if __name__ == '__main__':

    n = 53

    k = Solution()

    print (k.convertToTitle(n))