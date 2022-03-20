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
            prefixset= set([n&mask for n in nums])
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
    # 1 <= nums.length <= 2 * 105
    # 0 <= nums[i] <= 231 - 1
    # the len(nums) and nums[i] maybe very larger, so brutal solution(o()n*n) would be timeout.
    # have to find out a o(n) solution
    def findMaximumXOR1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1 <= nums.length <= 2 * 105
        # 0 <= nums[i] <= 231 - 1
        # the len(nums) and nums[i] maybe very larger, so brutal solution(o()n*n) would be timeout.
        # have to find out a o(n) solution
        #Runtime: 757 ms, faster than 94.37% of Python online submissions for Maximum XOR of Two Numbers in an Array.
        #Memory Usage: 28.5 MB, less than 90.54% of Python online submissions for Maximum XOR of Two Numbers in an Array.
        # greedy solution: want bit 31 is 1 and then bit 30 is 1...
        # bit rule: if a^b = c , a^c = b and b^c = a

        if len(nums) == 1: return nums[0]
        res = 0
        for i in range(31,-1,-1):
            #
            res <<= 1
            # create a set of values of i bits
            pre ={ n>>i for n in nums}
            #print('i-{} res-{} pre-{} type-{}'.format(i, res, pre, type(pre)))
            # any(iterable): return ture if any item is ture compared to all(iterable): all items should be true
            # res^p^1 = c -> res^p^c = 1
            res += any(res^p^1 in pre for p in pre)

        return res

    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bit rule: if a^b = c , a^c = b and b^c = a
        # description: https://kingsfish.github.io/2017/12/15/Leetcode-421-Maximum-XOR-of-Two-Numbers-in-an-Array/
        # Runtime: 960 ms, faster than 79.54% of Python online submissions for Maximum XOR of Two Numbers in an Array.
        # Memory Usage: 31 MB, less than 35.29% of Python online submissions for Maximum XOR of Two Numbers in an Array.
        # time: o(32n) = o(n) space: o(n)
        # greedy solution: use ans to keep the greedy result
        ans = mask = 0
        for x in range(31,-1,-1):
            # ans: the current best result of bit 31-(x+1)
            # ans: originally all 0
            # for example: 0b11111111111111111111111111110000
            mask += 1<<x
            # keep the left most x bit
            # set(): avoid repeatd calculating
            prefixSet = set([n&mask for n in nums])
            # tmp : the greedy best result of 31-x: keep the previous bit: 31-(x+1), set the x bit to 1
            tmp = ans | 1<<x
            for prefix in prefixSet:
                # if a^b = c , a^c = b and b^c = a
                # tmp ^ prefix = c ---> prefix^c = tmp
                if tmp ^ prefix in prefixSet:
                    ans = tmp
                    break
        return ans


if __name__ == '__main__':
    object = Solution()
    num = [3, 10, 5, 25, 2, 8]

    print(num)
    print('---Start---')
    r = object.findMaximumXOR(num)
    print(r)
    print('---End---')
