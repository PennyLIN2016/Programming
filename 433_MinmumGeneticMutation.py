class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Runtime: 104 ms, faster than 67.56% of Python online submissions for Maximum XOR of Two Numbers in an Array.
        #Memory Usage: 15.2 MB, less than 100.00% of Python online submissions for Maximum XOR of Two Numbers in an Array.
        res, mask =0,0
        # get the res bit by bit ,starting from the left significant bit
        # for bit 31 to bit 0
        for i in range(31,-1,-1):
            # the current mask: 0b
            # mask= mask +(1<<i)
            mask+=1<<i
            # get the most significant bits of nums,
            prefixset= set([n for n in nums])
            # tmp= res+ "1"in this bit
            tmp= res|1<<i
            for prefix in prefixset:
                # if a^b= c , a^c =b and b^c=a
                # tmp = prefix1^prefix2
                if tmp^prefix in prefixset:
                    # tmp have got the 1 in this bit
                    res= tmp
                    break
        return  res
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
    

if __name__ == '__main__':
    object = Solution()
    num = [3, 10, 5, 25, 2, 8]

    print(num)
    print('---Start---')
    r = object.findMaximumXOR(num)
    print(r)
    print('---End---')
