class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Runtime: 116 ms, faster than 63.83% of Python online submissions for Magical String.
        #Memory Usage: 13.1 MB, less than 100.00% of Python online submissions for Magical String.
        if n<=0:return 0
        if n<=3:return 1
        s=[1,2,2]
        i=2
        while len(s)<n:
            s+=[3-s[-1]]*s[i]
            i+=1
            print s
            print i
            print"---------"
        return s[:n].count(1)

   def magicalString(self, n: int) -> int:
        # Runtime: 166 ms, faster than 69.67% of Python3 online submissions for Magical String.
        # Memory Usage: 15.5 MB, less than 17.21% of Python3 online submissions for Magical String.
        # time: o(n) space: o(1)
        m = ['1', '2', '2']
        index = 2
        while len(m) < n:
            #print('index:{} m[index]:{} m[-1]: {}'.format(index, m[index], m[-1]))
            if m[-1] == '1':
                m += ['2'] * int(m[index])
            else:
                m += ['1'] * int(m[index])
            index += 1
            #print(''.join(m))

        return m[:n].count('1')

if __name__ == '__main__':
    object = Solution()
    A= 15


    print('---Start---')
    r = object.magicalString(A)
    print(r)
    print('---End---')
