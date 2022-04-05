
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

  def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Runtime: 732 ms, faster than 84.62% of Python online submissions for Number of Boomerangs.
        # Memory Usage: 41 MB, less than 37.36% of Python online submissions for Number of Boomerangs.
        # time: o(nlgn) space: o(n**2)
        import math

        n = len(points)
        if n < 3: return 0
        distances = [{} for _ in range(n)]
        for i in range(n-1):
            for j in range(i+1, n):
                # can't work in leecode running, python 2
                #d = math.dist(points[i], points[j])
                d = ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**0.5
                if d in distances[i]:
                    distances[i][d] += 1
                else:
                    distances[i][d] = 1
                if d in distances[j]:
                    distances[j][d] += 1
                else:
                    distances[j][d] = 1
        #print(distances)
        res = 0
        for v in distances:
            for i in v.values():
                if i > 1:
                    # A(N,2)
                    res += i * (i-1)
        return res

if __name__ == '__main__':
    object = Solution()
    num =  [[0,0],[1,0],[2,0]]



    print(num)
    print('---Start---')
    r = object.numberOfBoomerangs(num)
    print(r)
    print('---End---')
