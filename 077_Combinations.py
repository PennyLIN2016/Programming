class question(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def combine_next(n,k,cur_num,r):
            '''
            :param r:
            :param n:
            :param k:
            :return:
            '''
            if cur_num == []:
                start = 1
            else:
                start = cur_num[-1]+1

            if k == 1:
                for i in xrange(start,n+1):
                    r.append(cur_num +[i])
            else:
                for i in xrange(start,n+1):
                    tmp = cur_num[:]
                    tmp += [i]
                    combine_next(n,k-1,tmp,r)

        r = []
        cur_num = []
        combine_next(n,k,cur_num,r)
        return r

if __name__ == '__main__':

    k = 2
    n = 4
    t = question()
    r = t.combine(n,k)
    print  'result : ',r


