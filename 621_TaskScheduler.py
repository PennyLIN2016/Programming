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

if __name__ == '__main__':
    object = Solution()
    n1=["A","A","A","B","B","B",'C']
    n2= 1

    print('---Start---')
    print (n1)
    r = object.leastInterval(n1,n2)
    print(r)
    print('---End---')