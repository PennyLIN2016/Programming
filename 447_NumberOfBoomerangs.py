
import collections
class Solution(object):

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #Runtime: 720 ms, faster than 85.14% of Python online submissions for Number of Boomerangs.
        #Memory Usage: 12.1 MB, less than 16.67% of Python online submissions for Number of Boomerangs.
        # time: o(n**2) space0(n**2)
        res=0
        for x,y in points:
            tmpD= collections.defaultdict(int)
            for a,b in points:
                tmpD[(x-a)**2+(y-b)**2]+=1
            #   A(n, 2) = n * (n - 1)
            for d in tmpD:
                res+=tmpD[d]*(tmpD[d]-1)
        return res


if __name__ == '__main__':
    object = Solution()
    num =  [[0,0],[1,0],[2,0]]



    print(num)
    print('---Start---')
    r = object.numberOfBoomerangs(num)
    print(r)
    print('---End---')
