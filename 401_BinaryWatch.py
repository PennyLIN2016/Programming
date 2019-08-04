class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        #Runtime: 20 ms, faster than 67.46% of Python online submissions for Binary Watch.
        #Memory Usage: 11.7 MB, less than 83.33% of Python online submissions for Binary Watch.
        # iterator combinations solution: 
        from itertools import combinations
        def dfs(num,hour_bit,res):
            if hour_bit>num:return
            for hour in combinations([1,2,4,8],hour_bit):
                if sum(hour)>=12:continue
                for min in combinations([1,2,4,8,16,32],num-hour_bit):
                    if sum(min)>=60:continue
                    res.append("%d:%02d" % (sum(hour), sum(min)))
            dfs(num,hour_bit+1,res)

        res=[]
        dfs(num,0,res)
        return res



if __name__ == '__main__':
    object = Solution()
    s = 1


    r = object.readBinaryWatch(s)
    print(r)
    print('---End---')
