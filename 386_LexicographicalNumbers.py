class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #Runtime: 88 ms, faster than 93.45% of Python online submissions for Lexicographical Numbers.
        #Memory Usage: 18.2 MB, less than 30.36% of Python online submissions for Lexicographical Numbers.
        # time :o(n) space: o(n)
        if n<1: return []
        res= [0]*n
        cur= 1
        for i in range(n):
           res[i]= cur
           # cur+0/00/000 first
           if cur*10<=n:
               cur*=10
           else:
               
               if cur>=n:
                   cur //= 10
               cur+=1
               while cur%10==0:
                    cur//=10
        return res
       def lexicalOrder2(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        import heapq
        res = ['']*n
        for i in range(1, n+1):
            res[i-1] = str(i)
        heapq.heapify(res)
        # sorted(): O(n log n)
        return map(int, sorted(res))

if __name__ == '__main__':
    object = Solution()
    k = 57

    r = object.lexicalOrder(k)
    print(r)
    print('---End---')
