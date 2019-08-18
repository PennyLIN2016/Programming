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

if __name__ == '__main__':
    object = Solution()
    num = [3, 10, 5, 25, 2, 8]

    print(num)
    print('---Start---')
    r = object.findMaximumXOR(num)
    print(r)
    print('---End---')
