class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        #Runtime: 12 ms, faster than 90.51% of Python online submissions for Validate IP Address.
        #Memory Usage: 11.9 MB, less than 50.00% of Python online submissions for Validate IP Address.

        if len(IP)<7:return "Neither"
        v4L=IP.split('.')
        if len(v4L)==4:
            for v in v4L:
                if not v or not v.isdigit(): return "Neither"
                if v[0]=='0'and len(v)>1:return "Neither"
                if int(v)>255:return "Neither"
            return "IPv4"
        else:
            v6L=IP.split(":")
            if len(v6L)!=8:return "Neither"
            validChar = "0123456789abcdefABCDEF"
            for v in v6L:
                if len(v)>4 or not v:return "Neither"
                if any(c not in validChar for c in v): return "Neither"
            return "IPv6"

if __name__ == '__main__':
    object = Solution()
    A=  "2001:0db8:85a3:0:0:8A2E:0370:7334"
    print('---Start---')
    r = object.validIPAddress(A)
    print(r)
    print('---End---')
