class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count[i] : the number of inorder trees with i members
        count = [0 for i in xrange(n+1)]
        count[0]= 1
        count[1]= 1


        for i in xrange(2,n+1):
            # traaverse  j in 1~i as the root
            for j in xrange(1,i+1):
                count[i] += count[j-1]*count[i-j]

        return count[n]


if __name__ == '__main__':
    k = Solution()
    N = 3

    r = k.numTrees(N)
    print r





