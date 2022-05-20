import random
class Solution(object):
    #Runtime: 56 ms, faster than 18.37% of Python online submissions for Random Flip Matrix.
    #Memory Usage: 12.2 MB, less than 100.00% of Python online submissions for Random Flip Matrix.
    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.row=n_rows
        self.col=n_cols
        self.matrix=[]
        self.fliped=set()
        self.zero=n_cols*n_rows


    def flip(self):
        """
        :rtype: List[int]
        """
        k = random.randint(0,self.zero-1)
        while k in self.fliped:
            k= random.randint(0,self.zero-1)
        self.fliped.add(k)
        return [k/self.col,k%self.col]


    def reset(self):
        """
        :rtype: None
        """
        self.fliped.clear()
        
class Solution1:
    # timeout: 18 / 20 test cases passed.
    def __init__(self, m: int, n: int):
        self._m = m
        self._n = n
        self._zeroSet = set([i for i in range(m * n)])

    def flip(self) -> list[int]:
        import random
        if len(self._zeroSet) == 0:
            return None
        i = random.randint(0, len(self._zeroSet)-1)
        print('set: {} i: {}'.format(self._zeroSet, i))
        v = list(self._zeroSet)[i]
        self._zeroSet.remove(v)
        c, r = divmod(v, self._m)
        print('len: {} v: {} c: {} r: {}'.format(len(self._zeroSet), v, c, r))
        return [r, c]

    def reset(self) -> None:
        self._zeroSet = set([i for i in range(self._m * self._n)])

#Your Solution object will be instantiated and called as such:
obj = Solution(n_rows, n_cols)
param_1 = obj.flip()
obj.reset()
