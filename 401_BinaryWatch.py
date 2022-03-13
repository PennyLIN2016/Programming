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
    
    def readBinaryWatch2(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        #Runtime: 24 ms, faster than 65.06% of Python online submissions for Binary Watch.
        #Memory Usage: 13.8 MB, less than 15.66% of Python online submissions for Binary Watch.
        def dfs(lightNum,s,sum, visited):
            if lightNum == 0:
                return
            for i in [1,2,4,8,16,32]:
                if i in visited:
                    continue
                if sum + i > 59:
                    return
                if lightNum == 1:
                    if sum+i not in s:
                        s.append(sum+i)
                        continue
                else:
                    visited.add(i)
                    dfs(lightNum-1, s, sum+i, visited)
                    visited.remove(i)


        if turnedOn in [9,10]:
            return []
        hours = {
            0: ["0"],
            1: ["1", '2', '4', '8'],
            2: ["9", '10', "6", '5', '3'],
            3: ["7", '11' ],
        }
        sTurned = min(5, turnedOn)
        seconds = {0: ['00']}
        for i in range(1, sTurned+1):
            second = []
            visitedSet = set()
            dfs(i,second,0, visitedSet)
            seconds[i] = second
        #print(seconds)
        res = []
        for t in range(sTurned+1):
            h = turnedOn -t
            if h< 0 or h > 3:
                continue
            for i in hours[h]:
                for j in seconds[t]:
                    res.append('{}:{}'.format(i, str(j).zfill(2)))
        return res


if __name__ == '__main__':
    object = Solution()
    s = 1


    r = object.readBinaryWatch(s)
    print(r)
    print('---End---')
