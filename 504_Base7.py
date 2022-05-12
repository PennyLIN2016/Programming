class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        #Runtime: 16 ms, faster than 73.54% of Python online submissions for Base 7.
        #Memory Usage: 11.8 MB, less than 83.33% of Python online submissions for Base 7.
        if num<0:
            flag='-'
            num=- num
        else:
            flag=''
        res=''
        while num>=7:
            cur= num%7
            res= str(cur)+res
            num=int(num/7)
        if num!=0:
            res=flag+str(num)+res
        return res if res!='' else "0"

    def convertToBase7(self, num: int) -> str:
        # Runtime: 29 ms, faster than 91.35% of Python3 online submissions for Base 7.
        # Memory Usage: 13.9 MB, less than 12.53% of Python3 online submissions for Base 7.
        # time: o(lg7) space: o(1)
        if num == 0 : return '0'
        res = ''
        flag = 1 if num >= 0 else 0
        num = abs(num)
        while num > 0:
            quotient, reminder = divmod(num, 7)
            res = str(reminder) + res
            num = quotient
            #print('num: {} reminder: {}'.format(num, reminder))
        return res if flag == 1 else '-' + res
    
if __name__ == '__main__':
    object = Solution()
    A= -13
    print('---Start---')
    r = object.convertToBase7(A)
    print(r)
    print('---End---')
