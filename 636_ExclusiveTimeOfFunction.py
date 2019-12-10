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