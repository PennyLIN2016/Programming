import math
class question(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        visited_set = [0 for i in range(n)]
        fact_set = [math.factorial(n-1-i) for i in range(n)]

        s = ''
        pos_f = 0
        k -=1
        while 0 in visited_set:
                t = k/fact_set[pos_f]
                for j in range(n):
                    if visited_set[j] == 0:
                        if t == 0:
                            break
                        else:
                            t-= 1
                s+= str(j+1)
                k = k % fact_set[pos_f]
                visited_set[j] = 1
                pos_f+= 1

        return s


if __name__ == '__main__':

    n = 4
    k = 5
    t = question()

    r = t.getPermutation(n,k)
    print  'result : ',r


