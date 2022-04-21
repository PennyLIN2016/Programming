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
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        # Runtime: 2700 ms, faster than 99.12% of Python3 online submissions for Can I Win.
        # Memory Usage: 121.3 MB, less than 84.52% of Python3 online submissions for Can I Win.
        # dfs solution/ python 3 solution: time: o(n**2) space :o(n)
        # 2 status dp: one is saved by dp dict , the other one is implementated by dfs.
        # dfs深度优先搜索，搜索的过程中增加一个map来保存中途搜索结果避免重复搜索
        if desiredTotal <= maxChoosableInteger:
            return True
        if maxChoosableInteger*(maxChoosableInteger + 1)/2 < desiredTotal:
            return False
        # store the visited path result
        dp = {}
        # 目标值是否能用剩余的数字子集来加到。
        def dfs(choose, total, used):
            # used: the number set has been visited
            if used in dp:
                return dp[used]
            # try all possible choose in this turn
            for i in range(choose):
                # new syntax in python3 := that assigns values to variables as part of a larger expression.
                # ((cur := (1 << i)) & used) i have been used before: use a bit to mark if the value has been used.
                # if the i has been visited before, just skip
                # take i+1
                if not ((cur := (1 << i)) & used) \
                        and (total <= i + 1 or not dfs(choose, total - i - 1, used | cur)):
                    # check take i+1 solution
                    # total <= (i + 1)  : this turn, the starter win
                    # dfs(choose, total - i - 1, used | cur): used + take i+1: if true,  the peer can get total - (i+1)
                    # when starter takes i+1. 
                    dp[used] = True
                    return True
            dp[used] = False
            return False

        return dfs(maxChoosableInteger, desiredTotal, 0)

if __name__ == '__main__':
    object = Solution()
    A=  10
    B= 40
    print('---Start---')
    r = object.canIWin(A,B)
    print(r)
    print('---End---')
