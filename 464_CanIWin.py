class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        #Runtime: 400 ms, faster than 94.14% of Python online submissions for Can I Win.
        #Memory Usage: 30.7 MB, less than 100.00% of Python online submissions for Can I Win.
        # used[i]= keep the previous search result: True  or undefined
        # state: keep the used or not.
        # dfs solution
        used= {}
        def search(state,total):
            # for player 1
            for x in range(maxChoosableInteger,0,-1):
                # state&(1<<(x-1): get the value in the x-1 bit of state
                # the bit is 1 : used, 0: unused
                # if the bit is unused(=0).
                if not state&(1<<(x-1)):
                    if total+x>=desiredTotal:
                    # the first player can win by choosing x
                        used[state]= True
                        return True
                    break
            # for player 2
            for x in range(1,maxChoosableInteger+1):
                if not state &(1<<(x-1)):
                    # nstate= state+set (x-1)bit =1
                    nstate=state | (1<<(x-1))
                    if nstate not in used:
                        used[nstate]=search(nstate,total+x)
                    # player 2 can not win , so player 1 wins.
                    if not used[nstate]:
                        used[state]= True
                        return True
            used[state]=False
            return False
        if desiredTotal*2>maxChoosableInteger*(maxChoosableInteger+1):return False
        if desiredTotal<=maxChoosableInteger: return True
        # state=0 : no number is used, and current total =0
        return search(0,0,)


if __name__ == '__main__':
    object = Solution()
    A=  10
    B= 40
    print('---Start---')
    r = object.canIWin(A,B)
    print(r)
    print('---End---')
