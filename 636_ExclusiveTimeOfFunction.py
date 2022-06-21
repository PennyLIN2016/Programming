class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # Runtime: 68 ms, faster than 74.88% of Python online submissions for Exclusive Time of Functions.
        # Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Exclusive Time of Functions.
        # google solution: time: o(n) space(n)
        stack=[]
        res=[0]*n
        for log in logs:
            id, action,t= log.split(':')
            id,t=int(id),int(t)

            if action=='start':
                if stack:
                    # the stack only saves the start items. keep the start action
                    preid,pret=stack[-1]
                    res[preid]+=t-pret
                stack.append([id,t])
            else:
                # the top item should be the same function`s start.
                res[stack[-1][0]]+= t-stack[-1][1]+1
                stack.pop()
                if stack:
                    # for start from the end of the current function
                    stack[-1][1]=t+1
        return res
    
    ## ###python3
        def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        #Runtime: 90 ms, faster than 70.83% of Python3 online submissions for Exclusive Time of Functions.
        #Memory Usage: 14.1 MB, less than 34.22% of Python3 online submissions for Exclusive Time of Functions.
        # time: o(max(len(logs), n)) space: o(n)
        funcTime = [[] for _ in range(n)]
        stack = []
        for s in logs:
            sList = s.split(':')
            funcId, event, timeS = int(sList[0]), sList[1], int(sList[2])
            print('stack:{} funcTime:{}'.format(stack, funcTime))
            print('funcId: {} event:{} timeS: {}'.format(funcId, event, timeS))
            if event == 'start':
                if stack != []:
                    funcTime[stack[-1]][-1][1] = timeS-1
                funcTime[funcId].append([timeS, 0])
                stack.append(funcId)
            else:
                funcTime[stack[-1]][-1][1] = timeS
                stack.pop()
                if stack != []:
                    funcTime[stack[-1]].append([timeS+1, 0])

        print('funcTime: {}'.format(funcTime))
        res = [0] * n
        for i, v in enumerate(funcTime):
            for t in v:
                if t[0] <= t[1]:
                    res[i] += t[1] - t[0] + 1
        return res




if __name__ == '__main__':
    object = Solution()
    #n1=["0:start:0","1:start:2","1:end:5","0:end:6"]
    #n2= 2
    n1= ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
    n2=2

    print('---Start---')
    print (n1)
    r = object.exclusiveTime(n2,n1)
    print(r)
    print('---End---')
