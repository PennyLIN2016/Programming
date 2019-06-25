class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Runtime: 32 ms, faster than 93.95% of Python online submissions for Increasing Triplet Subsequence.
        #Memory Usage: 12.3 MB, less than 35.78% of Python online submissions for Increasing Triplet Subsequence.
        # greedy solution: time o(n), space o(1)
        min_1,min_2 = float('inf'),float('inf')
        for value in nums:
            # min_2 : the min value there is a value less then min_2 in front of min_2.
            if value > min_2 : return True
            # min_1 : the lest value
            if value < min_1:
                min_1= value
            # min_1 less than value, min_1 is in front of value and value less than min_2 so the value can replace min_2.
            elif value > min_1 and value< min_2:
                min_2 = value
        return False





if __name__ == '__main__':
    import sys
    k = Solution()
    l= [3,7,2,1,8]

    r = k.increasingTriplet(l)
    print(r)
    print('---End---')



