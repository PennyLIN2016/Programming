class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        #Runtime: 384 ms, faster than 81.80% of Python online submissions for Super Ugly Number.
        #Memory Usage: 14.9 MB, less than 68.50% of Python online submissions for Super Ugly Number.
        # time : o(n+k) space(n)
        import heapq
        # save the ugly numbers
        uglyNumber=[1]
        # yield the new ugly numbers, yield, not return, the return will be generated each calling time.
        def genMore(prime):
            for value in uglyNumber:
                yield value*prime
        # sort the ugly number
        heap_q= heapq.merge(*map(genMore,primes))
        while len(uglyNumber)<n:
            # each time will generate the heap_q again and get the latest next ugly number. heap_q would keep been added new elements.
            # get the next smallest ugly number
            tmp= next(heap_q)
            # avoid duplicated number.
            if tmp!=uglyNumber[-1]:
                uglyNumber.append(tmp)
        return uglyNumber[-1]


if __name__ == '__main__':
    k = Solution()
    s =  [2,7,13,19]
    j = 12
    print s
    r = k.nthSuperUglyNumber(j,s)

    print(r)
    print('---End---')



