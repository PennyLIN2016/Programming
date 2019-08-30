class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #Runtime: 376 ms, faster than 71.66% of Python online submissions for Minimum Number of Arrows to Burst Balloons.
        #Memory Usage: 17.3 MB, less than 75.00% of Python online submissions for Minimum Number of Arrows to Burst Balloons.
        # greedy approach: time o(nlgn+n)= o(nlgn) space:o(1)
        if not points: return 0
        # sorted by the right pos of the area
        points.sort(key = lambda x :x[1])
        right=points[0][1]
        res=1
        for i in range(len(points)):
            # if there is overlapping, the balloon can burst by the previous arrow.
            if right>=points[i][0]:
                continue
            right=points[i][1]
            res+=1
        return res



if __name__ == '__main__':
    object = Solution()
    num =  [[10,16], [2,8], [1,6], [7,12]]

    print(num)
    print('---Start---')
    r = object.findMinArrowShots(num)
    print(r)
    print('---End---')
