class Solution(object):
    def countBits1(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        #Runtime: 72 ms, faster than 71.72% of Python online submissions for Counting Bits.
        #Memory Usage: 15.7 MB, less than 60.56% of Python online submissions for Counting Bits.
        # math solution: time  o(n), space o(n) : but use in-bulit function
        import math
        res= [0]*(num+1)
        for i in range(1,num+1):
            if i%2 ==1:
                res[i]= res[i-1]+1
            else:
                res[i]= res[i - 2**int(math.log(i,2))]+1
        return res
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        #Runtime: 64 ms, faster than 94.44% of Python online submissions for Counting Bits.
        #Memory Usage: 15.9 MB, less than 7.98% of Python online submissions for Counting Bits.
        # time o(n) space o(n)
        res= [0]*(num+1)
        pre, paw2=1,1
        for i in range(1,num+1):
            if i ==paw2:
                pre,res[i]=1,1
                paw2<<=1
            else:
                res[i]= res[pre]+1
                pre+=1
        return res
    
    def countBits3(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #Runtime: 171 ms, faster than 24.65% of Python online submissions for Counting Bits.
        #Memory Usage: 17.4 MB, less than 31.96% of Python online submissions for Counting Bits.
        #brutal solution
        ans = [0]*(n+1)
        for i in range(1,n+1):
           ans[i] = bin(i).count('1')
        return ans
    
    def countBits4(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # dynamic solution: jus need to find the relationship between dp[i] and previous dp value
        # math point: n&(n-1) will remove the most right 1 bit. for example, 6(110)&5 = 4(100) remove the right most 1
        # time: o(n) space: o(n)
        dp= [0]*(n+1)
        for i in range(1,n+1):
            # math point: n&(n-1) will remove the most right 1 bit. 
            # for example, 6(110)&5 = 4(100) remove the right most 1
            dp[i] = dp[i&(i-1)]+1
        return dp

if __name__ == '__main__':
    k = Solution()
    l= 8

    r = k.countBits(l)
    print(r)
    print('---End---')



