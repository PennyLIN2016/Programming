import collections
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        #Runtime: 444 ms, faster than 15.96% of Python online submissions for 4Sum II.
        #Memory Usage: 34.4 MB, less than 25.00% of Python online submissions for 4Sum II.
        # time : o(n**2) space:o(n**2)
        # for a in A for b in B is different to for a,b in (A,B)
        ab=collections.Counter( a+b for a in A for b in B)
        res= [ab[-c-d] for c in C for d in D]
        return sum(res)



if __name__ == '__main__':
    object = Solution()
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]

    #print(num)
    print('---Start---')
    r = object.fourSumCount(A,B,C,D)
    print(r)
    print('---End---')
