class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        # Runtime: 1007 ms, faster than 65.28% of Python online submissions for Alert Using Same Key-Card Three or More Times in a One Hour Period.
        # Memory Usage: 44.1 MB, less than 88.89% of Python online submissions for Alert Using Same Key-Card Three or More Times in a One Hour Period.
        # hash map solution: time: o(nlgn) space: o(n)
        def inOneHour(time1, time2):
            h1, m1 = int(time1.split(':')[0]), int(time1.split(':')[1])
            h2, m2 = int(time2.split(':')[0]), int(time2.split(':')[1])
            h = h2 - h1 if h2 - h1 >= 0 else 24 + h1 - h2
            m = m2 - m1
            #print('time1: {} time2: {} h: {} m: {}'.format(time1, time2, h, m))
            return h * 60 + m <= 60
        l = len(keyName)
        records = {}
        for i in range(l):
            if keyName[i] not in records:
                records[keyName[i]] = [keyTime[i]]
            else:
                records[keyName[i]].append(keyTime[i])
        print(records)
        res = []
        for k, v in records.items():
            if len(v) < 3:
                continue
            v.sort()
            for j in range(2, len(v)):
                if inOneHour(v[j-2], v[j]):
                    res.append(k)
                    break
        #print(res)
        res.sort()
        return res


obj = Solution()

t1 = ["daniel","daniel","daniel","luis","luis","luis","luis"]
t2 = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
"""
t1 = ["alice","alice","alice","bob","bob","bob","bob"]
t2 = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]

t1= ["a","a","a","a","a","b","b","b","b","b","b"]
t2= ["04:48","23:53","06:36","07:45","12:16","00:52","10:59","17:16","00:36","01:26","22:42"]
"""
print(obj.alertNames(t1, t2))
