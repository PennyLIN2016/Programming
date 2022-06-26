class Solution(object):
    def subdomainVisits(self, cpdomains):
        # Runtime: 154 ms, faster than 5.32% of Python online submissions for Subdomain Visit Count.
        # Memory Usage: 13.6 MB, less than 52.47% of Python online submissions for Subdomain Visit Count.
        # time: o(n) space: o(m: valid domain name no)
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        cntDict = {}
        for v in cpdomains:
            print('v: {}'.format(v))
            values = v.split()
            count, domain = int(values[0]), values[1]
            domains = domain.split('.')
            strDom = ''
            print('count: {} domains: {}'.format(count, domains))
            for i in range(len(domains)-1 , -1, -1):
                if strDom == '':
                    strDom = domains[i]
                else:
                    strDom = '{}.{}'.format(domains[i], strDom)
                if strDom in cntDict:
                    cntDict[strDom] += count
                else:
                    cntDict[strDom] = count
        print(cntDict)
        res = []
        for k, value in cntDict.items():
            res.append('{} {}'.format(value, k))
        return res

obj = Solution()
t1 = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(obj.subdomainVisits(t1))
