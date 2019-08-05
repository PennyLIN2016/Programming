class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        #Runtime: 12 ms, faster than 90.89% of Python online submissions for Convert a Number to Hexadecimal.
        #Memory Usage: 11.7 MB, less than 53.85% of Python online submissions for Convert a Number to Hexadecimal.
        # bit operation solution: time: 0(1) space: o(n)
        k= 8
        flag=0
        res=''
        dict={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        while k:
            k-=1
            tmp= (num&0xf0000000)>>28
            if tmp!=0:
                flag=1
            if flag:
                if tmp<10:
                    res+=str(tmp)
                else:
                    res+=dict[tmp]
            num<<=4
        return res if res!=''else '0'









if __name__ == '__main__':
    object = Solution()
    num = 0

    print(num)
    r = object.toHex(num)
    print(r)
    print('---End---')
