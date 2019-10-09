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


if __name__ == '__main__':
    object = Solution()
    A= -13
    print('---Start---')
    r = object.convertToBase7(A)
    print(r)
    print('---End---')
