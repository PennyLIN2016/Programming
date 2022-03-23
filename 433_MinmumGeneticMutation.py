class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        # Runtime: 16 ms, faster than 87.50% of Python online submissions for Minimum Genetic Mutation.
        # Memory Usage: 13.5 MB, less than 33.75% of Python online submissions for Minimum Genetic Mutation.
        # dfs solution:

        # can't use res = float('inf') , res will be a local variant. can't be persist in dfs function
        res = [float('inf')]
        if not bank or not end in bank:
            return -1
        visited = set()

        def dfs(cur, cnt):
            for i in range(len(bank)):
                if bank[i] in visited:
                    continue
                if diffNum(bank[i], cur) != 1:
                    continue
                if bank[i] == end:
                    res[0] = min(res[0], cnt + 1)
                    return

                visited.add(bank[i])
                dfs(bank[i], cnt + 1)
                visited.remove(bank[i])

        def diffNum(s1, s2):
            c = 0
            for v1, v2 in zip(s1, s2):
                if v1 != v2:
                    c += 1
            return c

        if start in bank:
            bank.remove(start)
        dfs(start, 0)
        return -1 if res[0] == float('inf') else res[0]


if __name__ =='__main__':
    obj = Solution()
    t1 = "AAAAACCC"
    t2 = "AACCCCCC"
    t3 = ["AAAACCCC","AAACCCCC","AACCCCCC"]

    print('input: {}'.format(t1))
    r = obj.minMutation(t1, t2, t3)
    print('output: {}'.format(r))
    print('--------END--------')
