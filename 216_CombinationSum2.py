class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        #Runtime: 20 ms, faster than 84.65% of Python online submissions for Combination Sum III.
        #Memory Usage: 11.9 MB, less than 6.08% of Python online submissions for Combination Sum III.
        def findCom(start,res,k,n,tmp):
            if n< 0 or k <0:return
            if n ==0 and k==0:
                # guarantee the element unchanged after being pushed in to the res
                res.append(tmp+[])
                return
            for i in range(start,11-k):
                tmp.append(i)
                findCom(i+1,res,k-1,n-i,tmp)
                tmp.pop()
            return
        r= []
        findCom(1,r,k,n,[])
        return r




if __name__ == '__main__':

    t =  3
    s = 9
    print(t)
    object = Solution()
    r = object.combinationSum3(t,s)

    print(r)
    print('---End---')

