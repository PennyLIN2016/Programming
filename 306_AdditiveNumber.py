class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        #Runtime: 12 ms, faster than 99.33% of Python online submissions for Additive Number.
        #Memory Usage: 11.6 MB, less than 93.83% of Python online submissions for Additive Number.
        # time: o(n**2)
        # dfs look for the possible solution
        def checkSum(num1,num2,substr):
            tmp = str(num1+num2)
            if not substr.startswith(tmp):
                return False
            # get one solution and all done
            if tmp==substr:
                return True
            return checkSum(num2,num1+num2,substr[len(tmp):])

        if not num or len(num)<3 : return False
        for i in range(1,int(len(num)/2)+1):
            for j in range(i+1,len(num)):
                num1,num2  = int(num[:i]),int(num[i:j])
                # skip invalid number: start with 0 and is not 0
                if str(num1)!= num[:i] or str(num2)!=num[i:j]:
                    continue
                if checkSum(num1,num2,num[j:]):
                    return True
        return False

if __name__ == '__main__':
    s= "000"

    p = Solution()
    print(p.isAdditiveNumber(s))