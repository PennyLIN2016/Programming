import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # Runtime: 384 ms, faster than 64.80% of Python online submissions for Task Scheduler.
        # Memory Usage: 13.9 MB, less than 6.67% of Python online submissions for Task Scheduler.
        # My own solution: time:o(n) space : o(n)
        if n==0:return len(tasks)
        count=collections.Counter(tasks)
        print(count)
        maxCount=0
        keyCount={}
        for key in count:
            if count[key] in keyCount:
                keyCount[count[key]].append(key)
            else:
                keyCount[count[key]]=[key]
            maxCount=max(maxCount,count[key])
        print(keyCount)
        res= (n+1)*(maxCount-1)+ len(keyCount[maxCount])
        return max(res,len(tasks))
    
    
    #############python3
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Runtime: 435 ms, faster than 91.35% of Python3 online submissions for Task Scheduler.
        # Memory Usage: 14.2 MB, less than 99.21% of Python3 online submissions for Task Scheduler.
        # time: o(n + n + n) = o(n) space: o(n)
        if n == 0:
            return len(tasks)
        dic ={}
        for i in tasks:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1


        maxF = max(list(dic.values()))
        cnt = 0
        for v in dic.values():
            if v == maxF:
                cnt += 1
        return max((maxF-1)*(n+1) + cnt, len(tasks))

if __name__ == '__main__':
    object = Solution()
    n1=["A","A","A","B","B","B",'C']
    n2= 1

    print('---Start---')
    print (n1)
    r = object.leastInterval(n1,n2)
    print(r)
    print('---End---')
