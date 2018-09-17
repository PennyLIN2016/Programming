class Solution:
    # @param n, an integer
    # @return an integer
    # passed 93.88%
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result = result << 1
            result += n & 1
            n = n >> 1
        return result


if __name__ == '__main__':


    s= 43261596
    t = Solution()
    r = t.reverseBits(s)
    print(bin(s))
    if r == 964176192:
        print ("good")
    else:
        print(r)
        print(bin(r))