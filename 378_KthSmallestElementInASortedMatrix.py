import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # no good for duplicated elements: for example[[0,0,0],[2,7,9],[7,8,11]]
        n = len(matrix)
        visited= set()
        res=[]
        path=[[matrix[0][0],0,0]]
        while len(res)<k:
            next_path=[]
            path.sort()
            for value in path:
                if value[1]<n-1 and (value[1]+1,value[2]) not in visited :
                    next_path.append([matrix[value[1]+1][value[2]],value[1]+1,value[2]])
                    visited.add((value[1]+1,value[2]))
                if value[2]<n-1 and (value[1],value[2]+1) not in visited:
                    next_path.append([matrix[value[1]+1][value[2]],value[1],value[2]+1])
                    visited.add((value[1],value[2]+1))
                res.append(value[0])
            path = next_path

        return res[k-1]


    def kthSmallest1(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
    #Runtime: 360 ms, faster than 12.07% of Python online submissions for Kth Smallest Element in a Sorted Matrix.
    #Memory Usage: 17.4 MB, less than 19.12% of Python online submissions for Kth Smallest Element in a Sorted Matrix.
        nums = []
        for line in matrix:
            nums.extend(line)
        heapq.heapify(nums)
        res = 0
        for i in range(k):
            res = heapq.heappop(nums)
        return res
    
    def kthSmallest2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        if k == 1: return matrix[0][0]
        nums = []
        for v in matrix:
            nums.extend(v)
        heapq.heapify(nums)
        return heapq.nsmallest(k, nums)[-1]


if __name__ == '__main__':
    object = Solution()
    k = [
            [ 1,  5,  9],
            [10, 11, 13],
            [12, 13, 15]
        ]
    l = 8

    r = object.kthSmallest(k,l)
    print(r)
    print('---End---')
