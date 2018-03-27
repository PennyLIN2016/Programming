class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = {}
        for i,value in enumerate(nums):
            if value == 0:
                continue
            pos = visited.get(value)
            if pos == None:
                visited[value]= i
            else:
                nums[pos],nums[i] = 0,0

        return sum(nums)

if __name__ == '__main__':

    g = [4,6,4,4]

    k = Solution()

    r= k.singleNumber(g)
    print g
    print r
